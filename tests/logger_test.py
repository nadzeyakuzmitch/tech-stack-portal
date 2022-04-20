"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import os

from click.testing import CliRunner

runner = CliRunner()


def test_create_log_folder():
    """Testing if folder was created."""
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs')
    assert os.path.exists(logdir) is True


def test_create_debug_log_file(client):
    """Testing if folder was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/rootLogger.log')
    assert os.path.exists(logdir) is True


def test_create_requests_log_file(client):
    """Testing if folder was created."""
    response = client.get("/")
    assert response.status_code == 200
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../app/logs/appRequests.log')
    assert os.path.exists(logdir) is True
