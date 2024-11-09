# website/firebase_config.py
import json
import os

from firebase_admin import credentials, firestore, initialize_app



firebase_key_json = os.getenv('FIREBASE_KEY')
firebase_key_dict = json.loads(firebase_key_json)
# Initialize Firebase using the Firebase Admin SDK private key JSON file
cred = credentials.Certificate("firebase_key_dict")  # Update this path as needed
initialize_app(cred)

# Set up Firestore client
db = firestore.client()
