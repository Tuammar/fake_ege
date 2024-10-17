FROM python:3.12.1-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 6969

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
