import os
import logging
from parser import process_input_file_and_generate_csv

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Define paths to the spec and input files
spec_path = 'spec.json'
input_file = 'test_input.txt'

# Check if files exist
if not os.path.exists(spec_path):
    logging.error(f"Specification file '{spec_path}' not found.")
    exit(1)

if not os.path.exists(input_file):
    logging.error(f"Input file '{input_file}' not found.")
    exit(1)

# Run the processing function
try:
    process_input_file_and_generate_csv(spec_path, input_file)
    logging.info("Processing completed successfully. Check 'result.csv' for output.")
except Exception as e:
    logging.error(f"An error occurred during processing: {e}")
