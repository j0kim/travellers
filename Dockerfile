FROM python:3.9

COPY ./src /app
COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requiremnts.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--reload" ]

