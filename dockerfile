FROM python:3.7.13-slim-buster

WORKDIR /apps/mihate

COPY . .

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
