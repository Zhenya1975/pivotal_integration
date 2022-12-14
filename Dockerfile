FROM python:3.8
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
