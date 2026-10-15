FROM public.ecr.aws/docker/library/python:3.14-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:1.1.0 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /var/task
# COPY app.py requirements.txt ./
COPY * ./
RUN python3.14 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-b=:8000", "-w=1", "app:app"]
