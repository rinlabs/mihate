FROM python:alpine3.15

WORKDIR /apps/mihate

COPY . .

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
