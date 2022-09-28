FROM python:3.8-slim-buster
RUN apt update && apt install -y apt-transport-https ca-certificates sqlite3
WORKDIR /app
RUN mkdir db
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY *.py .
COPY *.sql .
ADD static static
ADD templates templates
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]