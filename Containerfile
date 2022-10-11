FROM python:3.10-slim-buster
COPY setup.py /src/
COPY dubilier /src/dubilier
WORKDIR /src
RUN apt-get update \
    && python3 -m pip install -U setuptools \
    && python3 setup.py install \
    && rm -rf /src
ENTRYPOINT ["dubilier"]
CMD ["bot", "run"]