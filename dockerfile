FROM python:3.11-rc-slim

WORKDIR /apps/mihate

COPY . .

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
