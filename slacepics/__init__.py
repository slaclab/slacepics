"""various EPICS tools

Module for various tools.  Currently only provides functions for dealing with
time.
"""

__author__ = 'Stephen Norum <snorum@slac.stanford.edu>'

# Re-import these for convenience
from .epicstime import *

__all__ = (epicstime.__all__)
