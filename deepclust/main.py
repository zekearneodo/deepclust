import sys
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QAction, QMainWindow
from PyQt5.QtCore import pyqtSlot

from deepclust import Ui_bout_search_setting

import glob
import os
from scipy.io import wavfile
import numpy as np

from swissknife.bci.core import expstruct as et


def load_single(wav_path, mmap=True):
    s_f, one_wav = wavfile.read(wav_path, mmap=mmap)
    return s_f, np.expand_dims(one_wav, axis=-1)


class BoutSearch(QWidget, Ui_bout_search_setting.Ui_bout_detect_form):
    def __init__(self, parent=None):
        super(BoutSearch, self).__init__(parent)
        
        self.setupUi(self)
        
        self.bird = None
        self.sess = None
        self.file = None
        
        self.s_f = None
        self.line_in_plot_span.setText(str(10000))

        self.fn = et.file_names('')
        
        selection_functions = {'select_bird': self.bird_change,
                                'select_sess': self.sess_change,
                                'select_file': self.file_change}
        for select_str in ['select_bird', 'select_sess', 'select_file']:
            q_box = getattr(self, select_str)
            q_box.currentIndexChanged.connect(selection_functions[select_str])
        
        self.update_birds_list()

        # Init plot widgets connections
        self.plot_bar.sliderMoved.connect(self.update_pos_slider)
        self.line_in_plot_start.returnPressed.connect(self.update_pos_text)
        self.line_in_plot_span.returnPressed.connect(self.update_plot_span)

    def update_birds_list(self):
        birds_list = et.list_birds(self.fn['folders']['rw'])
        self.select_bird.addItems(birds_list)

    def update_sess_list(self):
        self.fn = et.file_names(self.bird)
        sess_list = et.list_raw_sessions(self.bird, location='rw')[0]
        sess_list.sort()
        self.select_sess.addItems(sess_list)

    def update_files_list(self):
        self.fn = et.file_names(self.bird, self.sess)
        bout_folder = self.fn['folders']['rw']
        all_files = glob.glob(os.path.join(bout_folder, '*.wav'))
        all_files.sort()
        self.select_file.addItems(all_files)

    def update_plot(self):
        plot_start = self.plot_bar.value()
        plot_end = self.plot_span + plot_start
        self.dockWidgetContents.curve1.setData(self.x.flatten()[plot_start: plot_end])
    
    @pyqtSlot()
    def bird_change(self):
        self.bird = self.select_bird.currentText()
        self.update_sess_list()

    @pyqtSlot()
    def sess_change(self):
        self.sess = self.select_sess.currentText()
        self.update_files_list()

    @pyqtSlot()
    def file_change(self):
        self.file = self.select_file.currentText()
        ## reset_plot and scroll bar
        self.plot_reset()

    @pyqtSlot()
    def update_pos_slider(self):
        self.plot_start = self.plot_bar.value()
        self.line_in_plot_start.setText(str(self.plot_start))
        self.update_plot()

    @pyqtSlot()
    def update_pos_text(self):
        self.plot_bar.setValue(int(self.line_in_plot_start.text()))
        self.update_plot()

    @pyqtSlot()
    def update_plot_span(self):
        span_ms = int(self.line_in_plot_span.text())
        self.plot_span = int(span_ms * self.s_f * 0.001)
        self.plot_bar.setPageStep(int(self.plot_span * 0.9))
        self.plot_bar.setSingleStep(int(self.plot_span*0.09))
    
        self.update_plot()


    def plot_reset(self):
        self.s_f, self.x = load_single(self.file)
        
        self.plot_span = int(int(self.line_in_plot_span.text()) * self.s_f * 0.001)
        
        self.plot_bar.setMaximum(self.x.size - self.plot_span)
        
        self.plot_bar.setValue(0)
        self.line_in_plot_start.setText(str(0))

        self.update_plot()

        
        
    

        

class BoutSearchWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.bout_form = BoutSearch(parent=self)
        self.setGeometry(self.bout_form.frameGeometry())
        self.show()
        print('Bout search window init')
        self.bout_form.show()


class BoutFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # menu
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')

        exit_button = QAction('Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        # Textbox
        self.text_in = QLineEdit(self)
        self.text_in.move(20, 20)
        self.text_in.resize(280, 40)

        # Button 
        self.button = QPushButton('Tuvieja Button', self)
        self.button.setToolTip('Tu vieja')
        self.button.move(100, 70)


        # Connect button with on_click method
        self.button.clicked.connect(self.on_click)


        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tu vieja')


        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Buttion click')
        # question = 'you say {}'.format(self.text_in.text())
        # button_reply = QMessageBox.critical(self, 'quest box', question,
        #                             QMessageBox.Yes | QMessageBox.No,
        #                             QMessageBox.No)
        self.bout_search_window = BoutSearchWindow(self)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b_f = BoutFinder()

    sys.exit(app.exec_())