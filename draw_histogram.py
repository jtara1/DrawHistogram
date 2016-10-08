import matplotlib.pyplot as plt
import numpy as np
import time
import random
import sys
import csv
import json
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

py_version = sys.version_info[0]
FileNotFoundError = IOError if py_version==2 else FileNotFoundError



class WrongDataTypeError(Exception):
    """Raised when data type is invalid or not expected type"""
    def __init__(message):
        self.message = message


def load_data(filename):
    """Load data from `.csv` file or plain-text file.
    If `.csv` file given, all data should be in the first column and nothing
    else in the `.csv` file.

    :param filename: name of file to open and load data from
    """
    if filename.endswith('.csv'):
        data = []
        csv_reader = csv.reader(open(filename, newline='', encoding='utf-8'),
            delimiter=' ')
        for row in csv_reader:
            data.append(float(row[0]))
    else:
        try:
            data = json.loads(open(filename, 'r').read())
        except (FileNotFoundError, IOError):
            raise
        except (JSONDecodeError, ValueError):
            raise
        if not isinstance(data, list):
            raise WrongDataTypeError("Data from %s is not a %s." %
                (filename, "list"))
    return data


def draw_histogram(data, output_filename='histogram'):
    """Create a relative frequency histogram graph given a data set using
    matplotlib.pyplot `hist(...)` function and save the graph as an image file.

    :param data: list or ndarray containing floats or integers
    :param output_filename: name of image file created
    """
    n, bins, patches = plt.hist(data,
        weights=np.zeros_like(data) + 1. / len(data))
    print("Printing n, bins, and patches.")
    print(n, bins, patches)
    plt.title("Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Relative Frequency")
    plt.grid(True)

    fig = plt.gcf()
    fig.set_size_inches(12, 9)
    fig.savefig(output_filename, dpi=80)


if __name__ == "__main__":
    output_image_file = "histogram"

    # command line arguments were passed
    args = sys.argv
    if len(args) > 1:
        data_file = args[1]
        if len(args) == 3:
            output_image_file = args[2]
        data = load_data(data_file)
        print(data)
        draw_histogram(data, output_image_file)

    # no command line arguments passed
    else:
        data_filename = "example.data.txt"
        csv_filename = "example.data.csv"
        bad_data = "mumbo.txt"
        
        data = load_data(csv_filename)
        print(data)
        draw_histogram(data, output_image_file)
