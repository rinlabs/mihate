FROM python:slim-bullseye
RUN apt-get update && apt-get -y upgrade

RUN useradd --create-home mihate
WORKDIR /home/mihate
USER mihate

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /home/mihate/db
<<<<<<< HEAD
RUN chown mihate /home/mihate/db
=======
RUN chmod 644 /home/mihate/db
RUN chown mihate:mihate /home/mihate/db
>>>>>>> 559b53e89fc1dec71c3083e26e94254c04506e18

CMD ["python","mihate.py"]
