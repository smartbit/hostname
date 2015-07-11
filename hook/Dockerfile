FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get clean all

RUN pip install flask

ADD hook.py /tmp/hook.py

EXPOSE 5000

CMD ["python","/tmp/hook.py"]
