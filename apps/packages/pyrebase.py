import json
import pyrebase
    
firebase = pyrebase.initialize_app(json.load(open('config.json')))
pb_auth = firebase.auth()
realtime_db = firebase.database()
