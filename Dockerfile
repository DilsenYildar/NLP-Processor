FROM python:alpine3.7
MAINTAINER dilsenyildar
#RUN apt update -y && \
#    apt install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "NlpApi.py" ]