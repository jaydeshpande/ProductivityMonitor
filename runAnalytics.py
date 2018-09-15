import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def getDataDir():
    parent_directory = os.getcwd()
    scanner_start_time = datetime.today()
    timeLogDir = 'TimeLog'
    storage_folder = str(scanner_start_time.year) + '-' + \
                     str(scanner_start_time.month) + '-' + str(scanner_start_time.day)
    storage_directory = parent_directory + '/' + timeLogDir + '/' + storage_folder
    return storage_directory

def runAnalytics():
    storage_directory = getDataDir()
    data = pd.read_csv(storage_directory + '/' + 'timeHistory.csv')
    data['timeSpent'] = 2
    return data.groupby(['Application'])['timeSpent'].sum()

def createPie(data, debug = False):
    # Code from matplotlib examples
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(data.values, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(data.index.values[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, **kw)

    #ax.set_title("Application level time distribution")
    plt.savefig(getDataDir() + '/' + 'TimePieChart.png', dpi = 100)
    if debug:
        plt.show()

if __name__ == "__main__":
    createPie(runAnalytics())
