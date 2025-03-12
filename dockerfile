FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY db.py .
COPY static/ ./static/

EXPOSE 5000

CMD ["python3", "/app/app.py"]
