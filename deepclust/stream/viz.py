def plot_array(y, axis=0, fig_ax=None):
    amps = np.ptp(y, axis)
    y_plot = np.vstack([r/amps + np.arange(r.size) for r in y ])
    if not fig_ax:
        fig=plt.figure()
        fig_ax = fig.add_subplot(111)
    
    fig_ax.plot(y_plot);
    return fig_ax