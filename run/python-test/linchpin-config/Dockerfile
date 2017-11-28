FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y libbz2-1.0=1.0.6-8
RUN apt-get install -y libc6=2.23-0ubuntu9
RUN apt-get install -y libc6-i386=2.23-0ubuntu9
RUN apt-get install -y libffi6=3.2.1-4
RUN apt-get install -y libgcc1=1:6.0.1-0ubuntu1
RUN apt-get install -y libpython2.7-minimal=2.7.12-1ubuntu0~16.04.1
RUN apt-get install -y libpython2.7-stdlib=2.7.12-1ubuntu0~16.04.1
RUN apt-get install -y libssl1.0.0=1.0.2g-1ubuntu4.9
RUN apt-get install -y python-gobject-2=2.28.6-12ubuntu1
RUN apt-get install -y python-minimal=2.7.11-1
RUN apt-get install -y python2.7-minimal=2.7.12-1ubuntu0~16.04.1
RUN apt-get install -y zlib1g=1:1.2.8.dfsg-2ubuntu4.1
RUN apt-get install -y python-pip

RUN pip install numpy==1.13.3
RUN pip install scipy==1.0.0
RUN pip install sklearn==0.0

COPY python-test /python-test

ENTRYPOINT python python-test/demo.py