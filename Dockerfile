# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files into the container
COPY . .

# Install any required dependencies
RUN pip install -r requirements.txt  # If you have a requirements.txt file

# Run tests and then process input files
CMD ["sh", "-c", "python3 -m unittest parser_test.py && python3 run_test.py"]