# DrawHistogram
Creates image file of a histogram given a data set.

Load data from a (csv or text) file, create a relative frequency histogram graph
using matplotlib.pyplot module and save the histogram as an image.

## Requirements

Python 3

#### Modules

* matplotlib
* numpy
* PyQt4

## Usage

#### GUI

Start GUI by running through terminal then browse for a file to load data from
and click create histogram button.

    python main.py

![pic of gui](http://i.imgur.com/3taAoV1.png)

#### Command Line

CLI args take between 0 and 2 arguments. If there's no args, then the script
runs the function for the example csv data.

Syntax:

    python draw_histogram.py <data_file> [<output_image_file>]

Examples:

    python draw_histogram.py example.data.csv

    python draw_histogram.py example.data.csv my-histogram-chart
