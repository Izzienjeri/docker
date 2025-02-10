FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh .

# Grant execute permission to run.sh
RUN chmod +x run.sh

CMD ["./run.sh"]

