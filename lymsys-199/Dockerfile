FROM python:3.9

WORKDIR /

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["/bin/bash", "run.sh"]
