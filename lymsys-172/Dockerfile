FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && chmod +x run.sh

CMD ["/bin/bash", "/app/run.sh"]