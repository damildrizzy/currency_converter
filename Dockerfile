FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

# Allow installing dev dependencies to run tests
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app