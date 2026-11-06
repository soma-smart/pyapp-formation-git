FROM python:3.15-slim

WORKDIR /app
COPY pyapp/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY pyapp ./pyapp
ENTRYPOINT ["python", "pyapp/app.py"]
