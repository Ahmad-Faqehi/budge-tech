FROM tensorflow/tensorflow
WORKDIR /opt
RUN apt-get update -y
RUN apt install unixodbc-dev -y
RUN apt-get install libpq-dev -y
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "./server.py"] 
