# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory
COPY . .

# Install any necessary dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Command to run scripts
CMD ["/bin/bash", "run.sh"]
