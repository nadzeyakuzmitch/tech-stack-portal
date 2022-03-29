"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link active" href="/">Home</a>' in response.data
    assert b'<a class="dropdown-item" href="/git">Git</a>' in response.data
    assert b'<a class="dropdown-item" href="/docker">Docker</a>' in response.data
    assert b'<a class="dropdown-item" href="/flask">Python / Flask</a>' in response.data
    assert b'<a class="dropdown-item" href="/cicd">CI / CD</a>' in response.data
    assert b'<a class="dropdown-item" href="/pylint">Pylint & Others</a>' in response.data
    assert b'<a class="dropdown-item" href="/testing">AAA Testing</a>' in response.data
    assert b'<a class="dropdown-item" href="/oop">OOP</a>' in response.data
    assert b'<a class="dropdown-item" href="/solid">SOLID</a>' in response.data

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

def test_request_pylint(client):
    """This makes the pylint page"""
    response = client.get("/pylint")
    assert response.status_code == 200
    assert b"Pylint" in response.data

def test_request_testing(client):
    """This makes the testing page"""
    response = client.get("/testing")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_oop(client):
    """This makes the oop page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_solid(client):
    """This makes the solid page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the not found page"""
    response = client.get("/nonexistentpage")
    assert response.status_code == 404
