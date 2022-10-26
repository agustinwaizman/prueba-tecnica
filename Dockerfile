FROM python:3.11.0-alpine3.16

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

COPY . /app/

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver". "0.0.0.0:8000"]