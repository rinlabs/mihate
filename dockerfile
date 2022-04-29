FROM python:3.11-rc-slim

WORKDIR /apps/mihate

COPY . .

RUN pip install --upgrade pip

RUN apt install gcc

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
