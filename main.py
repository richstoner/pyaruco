__author__ = 'radlab'

from pyaruco import detect_markers

import logging
logging.basicConfig(level = logging.DEBUG)

import os
import sys
from numpy import array
from PIL import Image


# import ctypes
# import ctypes.util
# name = ctypes.util.find_library(r'C:\Users\radlab\drone_demo\native\build32\third-party\aruco-1.0.0\bin\Release\caruco')
# dll = ctypes.windll.LoadLibrary(name)

def main():
  """The main entry point of the program."""

  # Check the command-line arcuments.
  # if len(sys.argv) < 3:
  #   print('usage: aruco.py input.png output.png')
  #   sys.exit(1)

  # This is probably the simplest possible example.

  input_test = 'simple_board_1.png'
  output_test = 'test_out.png'

  im = Image.open(input_test).convert('RGB')
  arr = array(im)

  [m.draw(arr) for m in detect_markers(im)]
  Image.fromarray(arr).save(output_test, 'PNG')

if __name__ == '__main__':
  main()
