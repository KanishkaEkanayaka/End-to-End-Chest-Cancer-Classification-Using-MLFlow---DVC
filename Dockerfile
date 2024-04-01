FROM python:3.12.2-bookworm

RUN apt update -y && apt install aws-cli -y
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]