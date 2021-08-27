import firebase_admin
from firebase_admin import credentials

def setup():
    # Credentials for firebase
    cred = credentials.Certificate("./credentials/gluky-take-home-firebase-adminsdk-ps6ay-12bfd570fc.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'gluky-take-home'
    })