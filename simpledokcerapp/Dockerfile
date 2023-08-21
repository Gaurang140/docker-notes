FROM python:3.8-slim-buster


COPY  . /myapp /app

WORKDIR /app



RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "app.py"]
