import json
import os
from firebase_admin import credentials, firestore, initialize_app

# Load Firebase key from environment variable
firebase_key_json = os.getenv('FIREBASE_KEY')
if not firebase_key_json:
    raise Exception("FIREBASE_KEY environment variable is not set. Make sure to set this in Render.")

try:
    # Convert JSON string to dictionary and initialize Firebase
    firebase_key_dict = json.loads(firebase_key_json)
    cred = credentials.Certificate(firebase_key_dict)
    initialize_app(cred)
    db = firestore.client()
except json.JSONDecodeError:
    raise Exception("FIREBASE_KEY environment variable is not a valid JSON string.")
