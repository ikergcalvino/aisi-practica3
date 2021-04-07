FROM python:3.9.2-alpine
ENV FLASK_APP counter.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_DEBUG True
RUN pip install flask && pip install redis
RUN apk --no-cache add curl
WORKDIR /src
COPY src /src
EXPOSE 5000/tcp
ENTRYPOINT ["flask", "run"]
