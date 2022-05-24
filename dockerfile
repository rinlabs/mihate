FROM python:bullseye-slim
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN useradd --create-home mihate
WORKDIR /home/mihate
USER mihate

COPY . .

CMD ["python","mihate.py"]
