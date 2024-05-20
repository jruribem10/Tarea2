FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV CONTAINER_ID=docker_container

CMD ["python", "run.py"]
