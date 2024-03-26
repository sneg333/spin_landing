FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /land_spin
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
COPY . .
EXPOSE 8000
# Install system dependencies

RUN adduser --disabled-password land_spin-user

USER land_spin-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]