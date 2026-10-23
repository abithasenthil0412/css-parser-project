# CSS Parser

## Overview
A Python application that reads a CSS file, extracts selectors and their property-value pairs, and displays the results in JSON format.

## Technologies Used
- Python 3.13
- tinycss2 1.5.1

## Features
- Extracts CSS selectors and declarations.
- Converts CSS rules into structured JSON.
- Skips comments and whitespace.
- Handles missing input files with a clear error message.

## How to Run
1. Install dependencies:
   `python -m pip install -r requirements.txt`
2. Run the parser:
   `python parser.py`

## Design Decisions
I chose to extract selectors and property-value pairs because they provide meaningful, structured information about a stylesheet. JSON makes the extracted data easy to read and reuse.

## Edge Case
The parser checks whether the input file exists before reading it. If the file is missing, it reports a clear error rather than attempting to parse it.

## Future Improvement
Support nested rules inside at-rules such as `@media`.