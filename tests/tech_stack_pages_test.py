"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/flask">Python / Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI / CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to my" in response.data

def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_flask(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Flask" in response.data

def test_request_cicd(client):
    """This makes the cicd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Continuous" in response.data

def test_request_page_not_found(client):
    """This makes the not found page"""
    response = client.get("/nonexistentpage")
    assert response.status_code == 404
