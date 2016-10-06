import matplotlib.pyplot as plt
import numpy as np
import time
import random
import sys
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
    try:
        data = json.loads(open(filename, 'r').read())
    except (FileNotFoundError, IOError):
        raise
    except (JSONDecodeError, ValueError):
        raise
    if not isinstance(data, list):
        raise WrongDataTypeError("Data from %s is not a %s." % (filename, "list"))
    return data


def draw_histogram(data, output_filename='histogram'):
    plt.hist(g_numbs)
    plt.title("Gaussian Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)

    fig = plt.gcf()
    fig.set_size_inches(12, 9)
    fig.savefig(output_filename, dpi=80)


if __name__ == "__main__":
    # tests
    g_numbs = np.random.randn(1000)
    sample_data = [random.randint(0, 10) for i in range(1000)]
    data_filename = "example.data.txt"
    data = load_data("mumbo.txt")
    print(data)
    draw_histogram(sample_data, 'myhisto')
