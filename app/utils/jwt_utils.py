from flask_jwt_extended import create_access_token

def generate_token(username):
    return create_access_token(identity=username)
