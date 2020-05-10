import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.GUI()

    def GUI(self):
        canvas = Canvas(self)


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent):
        self.names = ["", ""]

        self.dates = ["1996-06-16", "2020-01-25"]

        # Make dates into format readable by numpy and plt
        self.dates = [datetime.strptime(d, "%Y-%m-%d") for d in self.dates]

        self.levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(self.dates) / 6)))[:len(self.dates)]
        self.fig, self.ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)

        # Mystery
        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        self.plot()

    def plot(self):

        markerline, stemline, baseline = ax.stem(self.dates, self.levels, linefmt="C3-", basefmt="k-", use_line_collection=True)

        plt.setp(markerline, mec="k", mfc="w", zorder=3)

        # Shift the markers to the baseline by replacing the y-data by zeros.
        markerline.set_ydata(np.zeros(len(self.dates)))

        # Annotation
        vert = np.array(['top', 'bottom'])[(self.levels > 0).astype(int)]
        for d, l, r, va in zip(self.dates, self.levels, self.names, vert):
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va=va, ha="right")

        # Interval
        ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=24))

        # Set label names instead of numbers
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))

        # Remove y-axis
        ax.get_yaxis().set_visible(False)

        # Remove borders
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)



if __name__ == '__main__':
    main()