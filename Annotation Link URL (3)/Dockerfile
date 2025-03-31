# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the solution, test files, and requirements.txt to the container
COPY solution.py /app/
COPY eval.py /app/
COPY run.sh /app/
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the unit tests
CMD ["/bin/bash", "run.sh"]