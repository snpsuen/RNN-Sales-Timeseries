FROM tensorflow/tensorflow

WORKDIR /tensorflow
EXPOSE 5005

pip install --upgrade flask numpy
COPY . .

ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=5005
