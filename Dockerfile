FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app ./app
COPY worker ./worker
COPY start.sh .

RUN chmod +x start.sh

ENV PYTHONUNBUFFERED=1

CMD ["./start.sh"]
