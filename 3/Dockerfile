FROM python:3.11

WORKDIR /app

COPY . /app

# Install dependencies

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_lg

COPY run.sh .

# Grant execute permission to run.sh

RUN chmod +x run.sh

CMD ["./run.sh"]

