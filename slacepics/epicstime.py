#!/usr/bin/env python
#
# Stephen Norum
# snorum@slac.stanford.edu

"""
Module for dealing with EPICS time
"""

import time
import calendar
import datetime

__all__ = ['system_to_epics_time', 'epics_to_system_time', 'EPICS_EPOCH', 'SYSTEM_EPICS_EPOCH_DELTA']

EPICS_EPOCH = '1990-01-01'
SYSTEM_EPICS_EPOCH_DELTA = calendar.timegm(time.strptime(EPICS_EPOCH, '%Y-%m-%d'))
    
def system_to_epics_time(seconds_past_system_epoch):
    """
    Return seconds_past_system_epoch converted to the number of seconds
    past the EPICS epoch.
    """
    return seconds_past_system_epoch - SYSTEM_EPICS_EPOCH_DELTA
    
def epics_to_system_time(seconds_past_epics_epoch):
    """
    Return seconds_past_epics_epoch converted to the number of seconds
    past the system's epoch.
    """
    return seconds_past_epics_epoch + SYSTEM_EPICS_EPOCH_DELTA
    