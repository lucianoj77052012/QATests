# Our requirements.txt requires Python >= 3.10. 3.12 will do.
FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .

# Make sure this runs first, since it's less frequently updated. Makes use of Docker cache for faster builds (literally 1 second vs 20+ seconds).
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./app.py"]