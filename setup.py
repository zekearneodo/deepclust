from setuptools import setup

setup(name='deepclust',
      version='0.1',
      description='Various tools to handle data and simmulations',
      url='http://github.com/zekearneodo/deepclust',
      author='Zeke Arneodo',
      author_email='earneodo@ucsd.edu',
      license='MIT',
      packages=['deepclust'],
      requires=['numpy', 'scipy', 'matplotlib', 'pyqt5'],
      zip_safe=False)
