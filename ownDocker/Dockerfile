

FROM jbflow/jibaek

COPY . /app

RUN pip install flask
RUN pip install requests

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

