FROM python:3.8
WORKDIR /opt
RUN apt-get update -y
RUN apt install unixodbc-dev -y
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "./server.py"] 
