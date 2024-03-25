FROM selenium/standalone-chrome as chrome
FROM python:3
COPY --from=chrome . /

COPY requirements.txt ./

RUN pip install -U -r requirements.txt

COPY . .

CMD ["python","main.py"]