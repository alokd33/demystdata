ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=11
ARG PYTHON_VERSION=3.9

#FROM tells Docker which image you base your image on
FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

#MAINTAINER alok <alokd3@gmail.com>
LABEL maintainer="alok <alokd3@gmail.com>"


COPY --from=py3 / /

ARG PYSPARK_VERSION=3.5.3
ARG parquet_tools_version=0.2.16

RUN pip freeze > requirements.txt

RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "vim"]
RUN ["apt-get", "-y", "install", "dos2unix"]

RUN dos2unix

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#RUN tells Docker which additional commands to execute.
# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN dos2unix /app/anonymize.sh

RUN mkdir /app/logs

RUN ["/bin/bash", "anonymize.sh"]

CMD ["/bin/bash"]