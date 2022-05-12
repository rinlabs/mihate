FROM python:bullseye

WORKDIR /apps/mihate

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
