import os
from pathlib import Path
import pytest

from flask_on_lambda.adapter.flask.app import create_app


@pytest.fixture()
def app(tmp_path):
    cwd = Path()
    os.chdir(tmp_path)

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here
    os.chdir(cwd)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
