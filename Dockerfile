FROM paulinus/opensfm-docker-base:python3

COPY . /source/OpenSfM

WORKDIR /source/OpenSfM

RUN pip3 install -r requirements.txt && \
    python3 setup.py build

RUN pip3 install pandas

RUN pip3 install PyQt5

ENV PATH $PATH:/source/OpenSfM/Scripts
ENV PYTHONPATH "${PYTHONPATH}:/source/OpenSfM"
