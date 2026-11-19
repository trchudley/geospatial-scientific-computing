"""
plotting.py

Plotting functions for the daily ERA5 Bristol temperature and precipitation record.
"""

import matplotlib.pyplot as plt


def plot_graph(df, write_to_file=None):
    """
    Plot daily mean temperature (line) and precipitation (bars) from an ERA5 dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe containing the columns 'date', 'temperature_2m_mean_degC',
        and 'precipitation_sum_mm'.
    write_to_file : str or pathlib.Path, optional
        If None (default), the plot is displayed as normal. If a file path is
        given, the plot is saved to that file and the figure is closed.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
        The temperature axes.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot precipitation as bars on a second y-axis that shares the same x-axis
    ax_precip = ax.twinx()
    ax_precip.bar(df["date"], df["precipitation_sum_mm"], color="tab:blue", alpha=0.5)
    ax_precip.set_ylabel("Precipitation (mm)", color="tab:blue")
    ax_precip.set_ylim(0, None)

    # Plot temperature as a line, and make sure it is drawn on top of the bars
    ax.plot(df["date"], df["temperature_2m_mean_degC"], color="tab:red", marker=".")
    ax.set_ylabel("Mean temperature (°C)", color="tab:red")
    ax.set_zorder(ax_precip.get_zorder() + 1)  # "z order" controls which layer is drawn on top
    ax.patch.set_visible(False)

    start = df["date"].min().strftime("%Y-%m-%d")
    end = df["date"].max().strftime("%Y-%m-%d")
    ax.set_title(f"Bristol ERA5 daily record: {start} to {end}")

    fig.autofmt_xdate()

    # Either save and close the figure, or leave it open to be displayed
    if write_to_file is not None:
        fig.savefig(write_to_file, dpi=100, bbox_inches="tight")
        plt.close(fig)

    return fig, ax
