
FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=nutritional_values_calculator.settings_docker

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]