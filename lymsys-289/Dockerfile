# Use a specific, stable version of Python
FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt first to leverage Docker cache when dependencies don't change
COPY requirements.txt .

# Install dependencies via pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY solution.py .
COPY eval.py .
COPY run.sh .


# Command to run when the container starts
CMD ["/bin/bash", "run.sh"]
