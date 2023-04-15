FROM amazonlinux:2023

RUN dnf install -y python python-pip

RUN mkdir -p /myapp
COPY ./myapp/requirements.txt /myapp/requirements.txt

RUN pip install -r /myapp/requirements.txt
COPY ./myapp /myapp

WORKDIR /myapp

EXPOSE 8000

CMD ["sh", "startup.sh"]
