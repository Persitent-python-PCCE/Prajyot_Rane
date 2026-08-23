import pytest

from app import create_app
from extensions import db


@pytest.fixture
def app():

    app = create_app()

    app.config.update(TESTING=True)

    with app.app_context():
        yield app
        db.session.rollback()


@pytest.fixture
def client(app):
    return app.test_client()
