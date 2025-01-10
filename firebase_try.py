import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyARHs2aKcxzHZGtvdo5Ef1uhHPWmZ9O-8s",
    'authDomain': "problem-f3394.firebaseapp.com",
    'projectId': "problem-f3394",
    'storageBucket': "problem-f3394.firebasestorage.app",
    'messagingSenderId': "523349010871",
    'appId': "1:523349010871:web:72baac3e7e8a2c647a2032",
    'measurementId': "G-SMSTBHKLZE",
    'databaseURL' : "https://console.firebase.google.com/u/0/project/problem-f3394/database/problem-f3394-default-rtdb/data/~2F?fb_gclid=CjwKCAiA-Oi7BhA1EiwA2rIu24iem37MR89z3eM60LOLxF5qBnbuH9lui9qNHH6FI9pZYtDvSENcLBoCGDsQAvD_BwE"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



def signup():
  print("Sign up..")
  email=input("Enter email :")
  password =input("Enter password :")
  try:
    user=auth.create_user_with_email_and_password(email, password)
    print("Successfully created account")
  except:
    print("Account already exists!")


def login():
  print("Log in...")
  email = input("Enter email :")
  password = input("Enter password :")
  try:
    login = auth.sign_in_with_email_and_password(email, password)
    print("Successfully logged in ")
  except:
    print("Account not found!")

ans=input("Are u a new user (Y/N) :" )
if ans =='y':
  signup()
elif ans == 'n':
  login()
else:
  print("Invalid input!")







