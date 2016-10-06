import matplotlib.pyplot as plt
import numpy as np
import time
import random


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
    draw_histogram(sample_data, 'myhisto')
