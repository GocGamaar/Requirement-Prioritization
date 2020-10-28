FROM python:3.9.0

RUN pip install numpy pandas jupyter
COPY ./jupyter_config.py /root/.jupyter/

RUN mkdir /code
WORKDIR /code
VOLUME /code

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888"]