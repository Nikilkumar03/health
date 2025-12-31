FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE ${APP_PORT}

USER nobody

CMD ["python", "app.py"]

HEALTHCHECK CMD curl -f http://localhost:${APP_PORT}/health || exit 1
