# access_control.py

verified_users = {
    "user1": "securetoken123",
    "admin": "adminpassword"
}

def authenticate_user(username, token):
    """
    Verify if the username and token match a verified user.
    """
    return verified_users.get(username) == token
