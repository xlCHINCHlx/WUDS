FROM kalilinux/kali-linux-docker

ADD wuds.tar.gz  /

RUN apt-get update && apt-get -y install python 

WORKDIR wuds/

CMD python kwuds.py
