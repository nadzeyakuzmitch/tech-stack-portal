import os

import click
from app.db import db
from flask.cli import with_appcontext

def db_folder_create():
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../../database')
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
        db.create_all()

def uploads_folder_create():
    root = os.path.dirname(os.path.abspath(__file__))
    uploadsdir = os.path.join(root, '../../uploads')
    if not os.path.exists(uploadsdir):
        os.mkdir(uploadsdir)

def logs_folder_create():
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)

@click.command(name='create-db')
@with_appcontext
def create_database():
    db_folder_create()

@click.command(name='create-uploads-folder')
@with_appcontext
def create_uploads_folder():
    uploads_folder_create()
    
@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    logs_folder_create()
