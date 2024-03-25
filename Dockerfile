FROM python:3.12

# install google chrome
# Check available versions here: https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable
ARG CHROME_VERSION="114.0.5735.198-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN apt -y update
RUN apt -y install /tmp/chrome.deb
RUN rm /tmp/chrome.deb
# install chromedriver
RUN apt-get install -yqq unzip
ARG CHROME_DRIVER_VERSION="114.0.5735.90"
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

COPY requirements.txt ./

RUN pip install -U -r requirements.txt

COPY . .

CMD ["python","main.py"]