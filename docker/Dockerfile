FROM fedora

RUN dnf -y update
RUN dnf install python3

ADD ./requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

WORKDIR /program