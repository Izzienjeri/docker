FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache when dependencies don't change
COPY requirements.txt .

# Install dependencies via pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Grant execute permission to run.sh
RUN chmod +x run.sh

# Command to run scripts
CMD ["/bin/bash", "run.sh"]