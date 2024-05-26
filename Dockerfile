FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget -O /usr/local/bin/chromedriver http://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip && \
    chmod +x /usr/local/bin/chromedriver

EXPOSE 80

ENV NAME World

CMD ["python", "run_tests.py"]
