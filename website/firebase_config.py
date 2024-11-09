# website/firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase using the Firebase Admin SDK private key JSON file
cred = credentials.Certificate("firebase_key.json")  # Update this path as needed
firebase_admin.initialize_app(cred)

# Set up Firestore client
db = firestore.client()
