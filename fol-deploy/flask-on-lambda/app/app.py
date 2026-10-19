import os

from flask_on_lambda.adapter.flask.app import create_app

is_lambda = bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))
instance_parent = "/tmp" if is_lambda else ""

app = create_app(instance_parent=instance_parent)
