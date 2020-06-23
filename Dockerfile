from ubuntu:latest

RUN apt-get update; \
    apt-get install curl -y; \
    apt-get install python -y;

RUN curl -k https://bootstrap.pypa.io/get-pip.py -o get-pip.py; \
    python get-pip.py

RUN pip install mysql.connector azure_storage_blob

ADD Blobkeda.py /usr/local/bin/

CMD python /usr/local/bin/Blobkeda.py
