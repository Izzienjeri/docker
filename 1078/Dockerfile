FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY solution.py .
COPY eval.py .

COPY run.sh .

CMD ["/bin/bash", "run.sh"]