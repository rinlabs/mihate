FROM python:3.11-rc-bullseye

WORKDIR /apps/mihate

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
