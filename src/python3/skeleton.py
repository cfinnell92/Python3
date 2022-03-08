"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = python3.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This skeleton file can be safely removed if not needed!

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
from multiprocessing import BoundedSemaphore
import sys
import math
from typing import List

from python3 import __version__

__author__ = "Cody"
__copyright__ = "Cody"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# 704. Binary Search
def findTargetFromList(self, nums: List[int], target: int) -> int:
    begIndex = 0
    endIndex = len(nums) - 1
    
    while begIndex <= endIndex:
        currIndex = math.floor((begIndex + endIndex) / 2)
        if nums[currIndex] == target:
            return currIndex
        elif nums[currIndex] > target :
            print("currIndex: ")
            print(currIndex)
            endIndex = currIndex - 1
        else:
            print("currIndex: ")
            print(currIndex)
            begIndex = currIndex + 1

    return -1


# 702. Search in a Sorted Array of Unknown Size
def findTargetFromUnknownSizeArrayObject(self, reader: 'ArrayReader', target: int) -> int:
    if reader.get(0) == target:
        return 0

    # search boundaries
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right <<= 1
        
    # binary search
    while left <= right:
        currIndex = left + ((right - left) >> 1)
        num = reader.get(currIndex)
        
        if num == target:
            return currIndex
        if num > target:
            right = currIndex - 1
        else:
            left = currIndex + 1

    return -1


# 1533. Find the index of the Large Integer
def updateLR(self, n, LR):
    mid = abs(-n>>1)-1
    return [LR[0],LR[0]+mid], [LR[0]+n-mid-1,LR[1]]        

def getIndex(self, reader: 'ArrayReader') -> int:
    n = reader.length()
    mid = abs(-n>>1)-1
    L = [0,mid]
    R = [n-mid-1,n-1]
    
    while L[1]-L[0]!=0 and R[1]-R[0]!=0:
        where = reader.compareSub(L[0],L[1],R[0],R[1])
        if where == 0:
            return L[1]
        elif where == 1:  # L
            n = L[1]-L[0]+1
            L,R = self.updateLR(n,L)
        elif where == -1:  # R
            n = R[1]-R[0]+1
            L,R = self.updateLR(n,R)
        
    where = reader.compareSub(L[0],L[1],R[0],R[1])
    if where == -1:
        return R[0]
    else:
        return L[1]
        

# 278. First Bad Version
def firstBadVersion(self, n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = left + (right - left) / 2
        if isBadVersion(mid) is True:
            right = mid
        else:
            left = mid + 1
    return int(left)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from python3.skeleton import fib`,
# when using this Python module as a library.


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for _i in range(n - 1):
        a, b = b, a + b
    return a


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="Python3 {ver}".format(ver=__version__),
    )
    parser.add_argument(dest="n", help="n-th Fibonacci number", type=int, metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m python3.skeleton 42
    #
    run()
