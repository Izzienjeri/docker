# Use the official Python image from the Docker Hub
FROM python:3.9-slim

RUN pip install pytest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the solution and test files to the container
COPY solution.py /app/
COPY eval.py /app/

# Run the unit tests
CMD ["/bin/bash", "run.sh"]

