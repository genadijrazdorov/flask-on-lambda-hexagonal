import os
from pathlib import Path

from flask_on_lambda.core.hello import hello

from flask import Flask


def create_app(test_config=None, instance_parent: str = ""):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        instance_path=Path(instance_parent).absolute() / "instance",
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # a simple page that says hello
    @app.route("/")
    def index():
        return hello()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
