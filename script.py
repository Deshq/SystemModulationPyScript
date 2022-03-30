import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from app.config import PATH_FOR_DOWNLOAD, FILE_NAMES


def convert_file_to_array(source_file: str) -> np.array:
    """
    reads numbers from txt file and writes to array
    :param source_file: path to file
    :return: array of numbers
    """

    data = []
    with open(source_file) as f:
        for line in f:
            data.append([float(x.replace(',', '.')) for x in line.split()])

    return data


def build_histogram(data: np.array, histogram_name: str):
    """
    :param data: array of numbers
    :param histogram_name: name of histogram
    """
    
    arr = np.array(data)
    # calculate mean and dispersion
    mean = np.mean(arr)
    var = np.var(arr)

    sns.set_style("darkgrid")
    ax = sns.histplot(data=arr, kde=True, bins='auto', color="pink")
    ax.set_title(histogram_name, fontsize=18)

    # build a rectangle in axes coords
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height

    ax.text(0.5*(left+right), -0.12*(bottom+top), f'Mean: {mean}, Dispersion: {var}',
            horizontalalignment='center',
            bbox=dict(facecolor='white',
                      alpha=0.5),
            fontsize=12,
            transform=ax.transAxes
            )

    plt.title(histogram_name)
    plt.show()


if __name__ == "__main__":

    try:
        for FILE_NAME in FILE_NAMES:
            data = convert_file_to_array(
                PATH_FOR_DOWNLOAD + FILE_NAME + '.txt')
            build_histogram(data, FILE_NAME)
    except Exception as ex:
        print(ex)
