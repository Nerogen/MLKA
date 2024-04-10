import os
import random

import matplotlib.pyplot as plt
import pandas as pd


class PlotDrawer:
    def __init__(self):
        self.__plot_folder: str = 'plots'
        self.__fig_size: tuple[float, float] = 8.0, 6.0
        if not os.path.exists(self.__plot_folder):
            os.makedirs(self.__plot_folder)

    def draw_plots(self, data_frame: pd.DataFrame, columns) -> list[str]:
        plot_paths: list[str] = []
        for column in columns:
            if column.lower() == "name":
                continue
            plt.figure(figsize=self.__fig_size)
            plt.plot(data_frame.index, data_frame[column], color=[random.random() for _ in range(3)])
            plt.title(f'{column} Plot')
            plt.xlabel('Index')
            plt.ylabel(column)
            plot_path: str = os.path.join(self.__plot_folder, f'{column}_plot.png')
            plt.savefig(plot_path)
            plt.close()
            plot_paths.append(plot_path)
        return plot_paths


def main() -> None:
    url: str = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
    plot_drawer: PlotDrawer = PlotDrawer()
    data_frame: pd.DataFrame = pd.read_json(url)
    columns: list[str] = data_frame.columns.tolist()
    plot_paths: list[str] = plot_drawer.draw_plots(data_frame, columns)
    print("Plots saved at:")
    for path in plot_paths:
        print(path)


if __name__ == '__main__':
    main()
