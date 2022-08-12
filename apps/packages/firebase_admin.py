from firebase_admin import credentials,auth
import firebase_admin

cred = credentials.Certificate('adminConfig.json')
firebase_admin = firebase_admin.initialize_app(cred)
