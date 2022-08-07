import pyrebase
config = {
  "apiKey": "AIzaSyALZS0dDe0Btyg_K7YFOOnWRNkJxapKMK0",
  "authDomain": "life-overseas.firebaseapp.com",
  "databaseURL": "https://life-overseas-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "life-overseas",
  "storageBucket": "life-overseas.appspot.com",
  "messagingSenderId": "2966303536",
  "appId": "1:2966303536:web:061114482e2d9d4c870ef5",
  "measurementId": "G-D52BSC4QRN",
};
firebase = pyrebase.initialize_app(config)
user_auth = firebase.auth()
realtime_db = firebase.database()
