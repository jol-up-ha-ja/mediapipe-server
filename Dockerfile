FROM python:3.10.9

COPY . /mania
WORKDIR /mania

RUN python3 -m pip install --upgrade pip
RUN	pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
CMD ["python3", "-m", "flask_server", "run", "--host=0.0.0.0", "--port=6000"]