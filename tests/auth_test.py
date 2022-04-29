"""This test the homepage"""

def test_auth_pages(client):
    """Check regular pages"""
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_deny_dashboard(client):
    """Deny dashboard"""
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_deny_songs_upload(client):
    """Deny songs upload"""
    response = client.get("/songs/upload")
    assert response.status_code == 302
