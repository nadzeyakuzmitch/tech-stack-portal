import os

import click
from flask.cli import with_appcontext


def folder_create():
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)


@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    folder_create()
