FROM python:slim-bullseye
RUN apt-get update && apt-get -y upgrade

RUN useradd --create-home mihate
WORKDIR /home/mihate
USER mihate

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","mihate.py"]
