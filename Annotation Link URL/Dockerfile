FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh
CMD ["./run.sh"]
