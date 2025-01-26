# Use an official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh .

RUN chmod +x run.sh

CMD ["./run.sh"]
