#!/usr/bin/env python
"""Calculate elapsed time for timestamps in logfile.

Syntax: q2.py"""
import re
from time import mktime, strftime, strptime, gmtime

index = 0
startingLine = None
runningLine = None

f = open("../../data/QuizData/Question2/engine.log", "r")


def processLines(startingLine, runningLine, index):
    # The first 16 characters in each line of the file are the timestamp.
    # Modify this for your needs.
    # DISCLAIMER: Adding year 2000 to surpass some machine limitations (mostly timestamps older than 1970)
    begin_time = "2000 " + startingLine.strip()[0:15]
    end_time = "2000 " + runningLine.strip()[0:15]

    # Format strings: http://docs.python.org/library/time.html#time.strftime
    firstTime = strptime(end_time, "%Y %b  %d %H:%M:%S")
    secondTime = strptime(begin_time, "%Y %b  %d %H:%M:%S")

    elapsed_sec = mktime(firstTime) - mktime(secondTime)
    elapsed_readable = strftime("%H:%M:%S", gmtime(elapsed_sec))

    print("Elapsed time (seconds) :", elapsed_sec)
    print("Start Cycle: {} Duration: {}:".format(index, elapsed_readable))
    pass


for line in f:
    # We try to match the "starting" filter
    matchedLine = re.search(".*starting nxengine.*", line)
    if matchedLine is not None:
        startingLine = matchedLine.string
    # We try to match the "running" filter
    matchedLine = re.search(".*nxengine is running.*", line)
    # We make sure that we are pairing an start with a running
    if matchedLine is not None and startingLine is not None:
        runningLine = matchedLine.string
    # When we have found both lines we calculate time
    if startingLine is not None and runningLine is not None:
        processLines(startingLine, runningLine, index)
        index += 1
        startingLine = None
        runningLine = None

input("Press enter to exit ;)")