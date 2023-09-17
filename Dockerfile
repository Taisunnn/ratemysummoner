FROM python:3.8

#spin up fastapi webserver, 

WORKDIR /code
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]