FROM python:3.9-slim

WORKDIR /app

COPY solution.py .
COPY eval.py .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pytest

COPY run.sh .

RUN chmod +x ./run.sh

CMD [ "/bin/bash", "run.sh" ]