# Shift Log Report Generator

A console application for logging and reviewing shift handoff reports.

## Problem

Shift workers need a fast, standardized way to log handoff details so the next
person and the chain of command have clear visibility into what happened
during a shift. This application walks the user through a guided,
validated menu to record shift details and saves each entry as a readable
report file for later review.

## Features

- Interactive menu: log a new shift, view saved reports, or quit
- Validated input for name, rank/grade (guided menu), email, and phone number
- Every entered value is echoed back for a Y/N confirmation before it's accepted
- Two objective, system-generated UTC timestamps (shift start and shift
  completion) recorded independently of the user's own input, as an
  accountability check
- Saved reports are plain text files in `logs/`, viewable from within the app

## Requirements

- Python 3

## Running it

From the project folder:

    python main.py

## Project structure

    main.py             Menu loop and program entry point
    logger.py           Input validation, report generation, and file I/O
    test_logger.py      Assertion-based tests for the validation logic
    logs/               Saved shift reports (.txt)
