FROM python:3.13-alpine
WORKDIR /farm-crm
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]