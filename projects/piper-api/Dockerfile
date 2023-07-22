FROM quay.io/pypa/manylinux_2_28_x86_64

RUN yum install -y espeak-ng

WORKDIR /piper-api

COPY requirements.txt .

RUN /opt/python/cp39-cp39/bin/python -m pip install --upgrade pip

RUN /opt/python/cp39-cp39/bin/python -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["/opt/python/cp39-cp39/bin/python", "-m", "flask", "--app", "piper_api.app", "run", "--host", "0.0.0.0", "--port", "5000"]
