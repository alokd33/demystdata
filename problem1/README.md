# Project Overview

This project is designed to parse fixed-width text files based on specified configurations in a JSON file and output the parsed data in a delimited format (CSV). Below are the key features and components of the project:

1. **File Structure**: The project contains six key files:
   - `parser.py`: The main script responsible for loading specifications, processing input files, and writing output.
   - `spec.json`: A JSON file defining column names, offsets for fixed-width parsing, and encoding settings.
   - `run_test.py`: A script to execute the parsing function and generate output, with logging for progress and errors.
   - `parser_test.py`: A unit test suite that verifies the functionality of the line-splitting method.
   - `test_input.txt`: A sample input file containing fixed-width data for testing purposes.
   - `Dockerfile`: Configuration for building a Docker container to run the application in a consistent environment.

2. **Fixed-Width Parsing**: The application reads fixed-width lines and splits them into segments based on the specified offsets, ensuring that empty fields are filled with underscores.

3. **CSV Output**: The parsed data is written to a CSV file named **`result.csv`** with the specified delimiter, and the option to include a header row based on the JSON specification. A sample output file, **`result_sample.csv`**, is provided for reference.

4. **Logging**: The application includes logging functionality to track the process, including warnings for existing output files and errors during file operations.

5. **Unit Testing**: The project includes a test suite (`parser_test.py`) to validate the parsing logic, ensuring robustness and reliability of the functionality.

6. **Docker Support**: The project can be run in a Docker container, providing an isolated environment for execution and simplifying dependencies.

7. **Command-Line Interface**: The application can be run with command-line arguments to specify the input file and the specification file, making it flexible for various use cases.

8. **Encoding Support**: The application handles different text encodings (specified in the JSON file) to ensure correct reading and writing of files.

9. **Installation and Usage**: Detailed instructions for setting up the environment and running the application are included, making it user-friendly for developers.

## How It Works
```plaintext
+------------------+
|                  |
|   test_input.txt |   (Input: Fixed-width text file)
|                  |
+--------+---------+
         |
         | Reads input file
         |
         v
+------------------+
|                  |
|   parser.py      |   (Main processing script)
|                  |
|  +-----------+   |
|  | load_spec |   |   (Load specifications from spec.json)
|  +-----------+   |
|         |        |
|         v        |
|  +-----------+   |
|  | split_line|   |   (Split lines based on offsets)
|  +-----------+   |
|         |        |
|         v        |
|  +-----------+   |
|  | write_csv |   |   (Write output to result.csv)
|  +-----------+   |
|                  |
+--------+---------+
         |
         | Generates output file
         |
         v
+------------------+
|                  |
|   result.csv     |   (Output: Delimited CSV file and sample file result_sample.csv)
|                  |
+------------------+

```

## How to Build Docker
1. Create a new directory:
```bash
mkdir docker_problem1
```
2. Change to that directory
```bash
cd docker_problem1
```
3. Clone the repository
```bash
git clone https://github.com/alokd33/demystdata.git
```
4. Change to the project directory:
```bash
cd demystdata/problem1
```
5. Build the Docker image:
```bash
docker build -t my_parser_app .
```

## How to Run Docker
To run the application and generate the output, use the following command:
```bash
docker run --rm -v $(pwd):/app my_parser_app
```
## How to Validate the Output
To see the output, check the first line for the header and subsequent lines for data:
```bash
cat result.csv
```
Note: If you need more testing, update test_input.txt and spec.json, and then run:
```bash
docker run --rm -v $(pwd):/app my_parser_app
```

## How to See Docker Info
1. List all containers
```bash
docker ps -a  # Get running CONTAINER ID
```
2. Stop a specific container
```bash
docker stop <CONTAINER ID>
```
3. Remove a specific containe
```bash
docker rm <CONTAINER ID>
```
