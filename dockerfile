FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY static/ ./static/
RUN mkdir rooms

EXPOSE 5000

CMD ["python3", "/app/app.py"]
