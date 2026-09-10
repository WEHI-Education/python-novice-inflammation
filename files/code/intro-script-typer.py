# Second iteration of the intro-script using the 'typer' package.
# You will need to install typer into your environment:
#    `conda activate carpentries`
#    `pip install typer`
#     OR `conda install typer`
# The script can be run with the command:
#     `python intro-script-typer.py --figure swc-python/data/inflammation-02.csv`

from pathlib import Path
from typing import Annotated

import matplotlib.pyplot
import numpy
import typer
from matplotlib.figure import Figure
from numpy import ndarray


def main(
    is_figure: Annotated[bool, typer.Option("--figure/--stats")],
    input_csv: Annotated[Path, typer.Argument()],
):
  print("loading data...")
  data = numpy.loadtxt(input_csv, delimiter=',')

  if is_figure:
    figure = make_figure(data)
    print("writing figure to output.png ...")
    figure.savefig("output.png")
  else:
    stats = make_stats(data)
    print("writing stats to output.csv ...")
    numpy.savetxt("output.csv", stats, header="mean,max,min", delimiter=",")

  print("done!")


def make_figure(data: ndarray) -> Figure:
  fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

  axes1 = fig.add_subplot(1, 3, 1)
  axes2 = fig.add_subplot(1, 3, 2)
  axes3 = fig.add_subplot(1, 3, 3)

  axes1.set_ylabel('average')
  axes1.plot(numpy.mean(data, axis=0))

  axes2.set_ylabel('max')
  axes2.plot(numpy.max(data, axis=0))

  axes3.set_ylabel('min')
  axes3.plot(numpy.min(data, axis=0))

  fig.tight_layout()
  return fig

def make_stats(data: ndarray) -> ndarray:
  return numpy.column_stack([
    numpy.mean(data, axis=0),
    numpy.max(data, axis=0),
    numpy.min(data, axis=0)
  ])

if __name__ == "__main__":
  typer.run(main)
