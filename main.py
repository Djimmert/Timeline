import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

names = ["", ""]


dates = ["1996-06-16", "2020-01-25"]

# Make dates into format readable by numpy and plt
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/6)))[:len(dates)]

fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)

markerline, stemline, baseline = ax.stem(dates, levels, linefmt="C3-", basefmt="k-", use_line_collection=True)

plt.setp(markerline, mec="k", mfc="w", zorder=3)

# Shift the markers to the baseline by replacing the y-data by zeros.
markerline.set_ydata(np.zeros(len(dates)))

# Annotation
vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
for d, l, r, va in zip(dates, levels, names, vert):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3), textcoords="offset points", va=va, ha="right")

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

if __name__ == '__main__':
    plt.show()