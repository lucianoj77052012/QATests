# Our requirements.txt requires Python >= 3.10. 3.12 will do.
FROM python:3.12-slim

ENV CHROME_VERSION=156.0.8078.47

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y wget && apt-get install -y zip

# To open Chrome in headerless mode within the container, you need Chromium. You don't need the binary itself.
RUN apt-get install -y chromium

RUN wget https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip \
  && unzip chromedriver-linux64.zip && rm -dfr chromedriver_linux64.zip \
  && mv ./chromedriver-linux64/chromedriver ./chromedriver \
  && chmod +x ./chromedriver

COPY requirements.txt .

# Make sure this runs first, since it's less frequently updated. Makes use of Docker cache for faster builds (literally 1 second vs 20+ seconds).
RUN pip install -r requirements.txt

RUN mkdir -p ./reports

COPY . .

ENTRYPOINT ["pytest"]