import os
from pathlib import Path

from flask_on_lambda.adapter.flask.app import create_app

is_on_lambda = os.environ.get("AWS_LAMBDA_FUNCTION_NAME", False)

app = create_app(instance_parent="/tmp" if is_on_lambda else Path())
