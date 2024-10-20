"""
## Json spec file refer at https://github.com/DemystData/code-kata/blob/data-eng/spec.json
{
    "ColumnNames": ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"],
    "Offsets": ["5","12","3","2","13","7","10","13","20","13"],
    "FixedWidthEncoding":"windows-1252",
    "IncludeHeader":"True",
    "DelimitedEncoding":"utf-8"
}
"""
import logging
import csv
import json
import argparse
import os


def load_specification_from_json(spec_path):
    """
    Loads and parses the specification JSON file.

    Args:
        spec_path (str): Path to the specification JSON file.

    Returns:
        tuple: A tuple containing:
            - list: Column names as strings.
            - list: Offsets as integers.
            - bool: Include header flag.
            - str: Input encoding.
            - str: Output encoding.
    """
    column_names = []
    offsets = []
    include_header = False
    input_encoding = None
    output_encoding = None

    try:
        with open(spec_path) as spec_file:
            spec = json.load(spec_file)
            column_names = spec.get('ColumnNames')
            offsets = [int(s) for s in spec.get('Offsets')]
            input_encoding = spec.get('FixedWidthEncoding')
            include_header = spec.get('IncludeHeader').lower() == 'true'
            output_encoding = spec.get('DelimitedEncoding')

        return (column_names, offsets, include_header, input_encoding, output_encoding)

    except Exception as err:
        logging.error('Cannot parse the spec: %s', err)
        raise

def split_line_into_segments(textline='', offsets=[]):
    """
            Splits a line of text into segments based on fixed widths provided in offsets.

            Args:
                textline (str): The input text line to be split.
                offsets (list): A list of integer widths defining where to split the line.

            Returns:
                list: A list of strings split according to the specified widths, with empty
                      values replaced by underscores.

            Raises:
                ValueError: If offsets are not valid integers or if textline is empty.

            Example:
                Given the line "hello world 4567" and offsets [5, 12, 15]:
                - The function will split the line into segments:
                  1. "hello" (first 5 characters)
                  2. " world" (next 7 characters)
                  3. " 4567" (next 3 characters, note the leading space)

                The result will be:
                ['hello', 'world', '4567']

                If the input line is "hello     " and offsets are [5, 12]:
                - The function will produce:
                  1. "hello" (first 5 characters)
                  2. "     " (next 7 characters, all spaces)

                The result will be:
                ['hello', '_'] (the empty value is replaced with an underscore)

                Zero-Based Indexing
                Offset 0 to 5: "hello" (characters 0 to 4)
                Offset 5 to 12: " world" (characters 5 to 11)
                Offset 12 to 15: " 4567" (characters 12 to 14)
            Note:
                - If any segment exceeds the line length, it will result in a segment with trailing spaces or empty.
                - The final segment will not be processed to a new split unless specified by the offsets.
    """
    if not textline:
        logging.error("Input textline is empty.")
        raise ValueError("Input textline cannot be empty.")

    if not all(isinstance(n, int) for n in offsets):
        logging.error("Offsets must be a list of integers.")
        raise ValueError("Offsets must be a list of integers.")

    line_segments = []
    start = 0

    for offset in offsets:
        segment = textline[start:start + offset]  # Extract the segment based on offset
        segment = segment.strip()  # Remove leading and trailing spaces
        line_segments.append(segment if segment else '_')  # Replace empty segments with '_'
        start += offset

        # Stop if we've reached the end of the line
        if start >= len(textline):
            break

    # Fill any remaining segments with underscores to match the number of offsets
    while len(line_segments) < len(offsets):
        line_segments.append('_')

    return line_segments


def process_input_file_and_generate_csv(spec_path, input_file, output_file='result.csv', delimiter=';', overwrite=True):
    """
    Processes the input file based on the provided specification and writes
    the output to a CSV file.

    Args:
        spec_path (str): Path to the specification JSON file.
        input_file (str): Path to the input text file to be processed.
        output_file (str): Path to the output CSV file (default is 'result.csv').
        delimiter (str): The delimiter to use in the output CSV file (default is ';').
        overwrite (bool): If True, will overwrite the existing output file (default is True).
    """
    column_names, offsets, include_header, input_encoding, output_encoding = load_specification_from_json(spec_path)

    # Check if the file exists and handle overwrite option
    if not overwrite and os.path.exists(output_file):
        logging.warning(f"{output_file} already exists and will not be overwritten.")
        return

    try:
        with open(output_file, 'w', encoding=output_encoding) as csv_file:
            writer = csv.writer(csv_file, delimiter=delimiter)

            with open(input_file, 'r', encoding=input_encoding) as f:
                if include_header:
                    writer.writerow(column_names)  # Write header

                for line in f:
                    line = line.rstrip('\n')  # Remove newline characters
                    if len(line) == 0:
                        continue  # Skip empty lines

                    splitted_line = split_line_into_segments(line, offsets)
                    writer.writerow(splitted_line)

    except Exception as err:
        logging.error('File IO error: %s', err)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text to csv')
    parser.add_argument('spec', metavar='F', type=str, help='spec')
    parser.add_argument('file', metavar='F', type=str, help='textfile')
    args = parser.parse_args()
    spec = args.spec
    file = args.file
    process_input_file_and_generate_csv(spec, file)