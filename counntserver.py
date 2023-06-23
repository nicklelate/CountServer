import cvlib as cv
import datetime
import time
import pyrebase
from firebase import firebase
import cv2
from cv2 import *
# python -m pip install

url = 'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/'
messenger = firebase.FirebaseApplication(url)

config = {

    "apiKey": "AIzaSyDUjAaxdmzaS-Pllrm-W8zfTn_fiQyd39A",
    "authDomain": "timesensor-cbe40.firebaseapp.com",
    "databaseURL": "https://timesensor-cbe40-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "timesensor-cbe40",
    "storageBucket": "timesensor-cbe40.appspot.com",
    "messagingSenderId": "93578226868",
    "appId": "1:93578226868:web:f7e1af24f5f26a668e3be1",
    "measurementId": "G-RGM0S2D23H",
    "serviceAccount":{
        "type": "service_account",
        "project_id": "timesensor-cbe40",
        "private_key_id": "687de6d6b64c721f80a72c1d218b451b8ee7923c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeC28zS1DMabsp\nXZCSp3jV5xBr8Dnkbg1Ko3G3ntTHd+8JmfPyaVYFa3aUA9NXQz2rI+Tjvdr6+ndR\nBff97OLT5C2YbSOM0/ARgbLjsvV7Ek/8v6274rLfMTcaK6IanpmLcNajBnY1Y6+1\nHuGnm0usVNFc6qWuIuiVynHCV/6Z6FsSzomYWdD6/N1g7Rraq4fGn8E0fBF1VdLr\nwGAS8+xHf72bwKzzs26UagslhGyy5Yu+mGqEeQHtZdHkDnEHUTeiHnT9wA3lGrcm\nY1HzoMjBvyCrtX12XAJipjBHOX9Oem6WACnyfFZF2ACHWGRq34Yz4eBEPFwxmmuY\n/Nzhm9pvAgMBAAECggEAC1J4Ye1YWXyNmvYIAGmc/33xMDpie1ni++Dfqa7oQW33\nIvHzhv9C2VqMgSgRAORhS5xjrmkQggBlgdlyna9VxKZJGe1fqZwZS7fF8AgHDA0Q\ny+OTd61S8ShecTKFB3ErQNERn1Y8K7D7incu5Un7ztm4sfZhbis0DF8XbTvOkon0\n/4Ml6TUSTbTxOtLkaY+KTuOKJLv/tR87Tp3wqX8sAWrK4LjdXbiO78a0wbHaQXNb\nPgFg06DbmRLnkwJek81+fONA3/nZpCTjcoz9H12L7acqH/d60NQedORGrKCD1nul\nCxXHG6oqDGStSGpZGMo6S3xRSXb+KGYtNf6iliEdwQKBgQDO0j4sZwmVtU/fFpDK\n976v3OOeJjGsGEO4JrcHfJ9B9JlNOq1y4BasH0Go05tE2+bFSIYCjcJbdRqCmlJE\nYdaGgBDIJXU7r46cQBd0ymkhcZgt0Tpaal9nAeM8cdb2HSuTJmsFBBsyfP6Cf4s6\nOO/KzsIUNfTPvQto4hUCPMEG4QKBgQDDoAf4oIwusFC9Fwt908T98udR4Pi/DWlS\nqsvFV8xgkosJg9J/5IGD5eH2OjaV22DiadMAXSF0XTjKP8KFn6QdrHRqT4BVBH/b\n5eQQZW6nhTNyferRdX+QJR/jeyJHYTXNDkNmLL4RYP4K3cgszgbmplvJxw2bpY8y\nCKYQXXEbTwKBgAGX+ySqcpd1uzTT3q/BsvV19UcNskpKMZNksPpcynleoiPHNPjy\noxoWb5IWd1bTfva8NVQltX6w61BgUgv22QlWSUrRhxK7qpSnpcafnKnGT07jEtkJ\ngsyvZgncMrTYyrIqlJ6IRpFgBzIIO5FqSOa+Kx6uv8EuCr13KIRI5Y/hAoGAXPFO\neDjHAXOxmHU3d3vCzyi18HfjltnnXWhaUhNJveRB/K5Nt4e4ZRM2TUcRIhfNqyS+\nJCEbQO79iVHLuLLFRXfnA49sGHh/ytkphwS6Ews9Czt58jRR/Ak3YlvhSGqOJjON\noCDH2PftGvqOHYNxUepeF7rj4zxAkXP8ei/7Cg8CgYEAqu5hV5WnZ2sKyfijWIK2\ny53RcHP92YDVG9xw9kLoAQodP6Tz15xY6TWqPPY8BGzC2nsGm3mBh4lfyxuhit7p\n2IILRwQk/C9Cf8l+NJPXduiwKRxpPTnggmDznEFsUqChA4VmFqza+JgjSkOkO44P\nBcyP5yOAY54AHBLtzXDntkk=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-30mf0@timesensor-cbe40.iam.gserviceaccount.com",
        "client_id": "110605118277163427239",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-30mf0%40timesensor-cbe40.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
        }
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()
# storage.child("818_room.png").download("818_room.png","818_room.png")

boardtime = db.child("Time").get()
# for t in boardtime.each():
#     data = t.val()
# timenow = data['PictureTimestamp']
# print(timenow)
# print(data)
timelast = '0'

while True:
    data = boardtime.val()
    for t in boardtime.each():
        data = t.val()
    timenow = data['PictureTimestamp']
    if timenow != timelast:
        storage.child("818_room.png").download("818_room.png","818_room.png")
        img = cv2.imread("818_room.png")
        box,label,count = cv.detect_common_objects(img)
        count = 0
        for i in label:
            if i == 'person':
                count += 1
        x = datetime.datetime.now()
        print("there are " + str(count) + " people.")
        engineer = {'Timestamp':x,'People':count}
        result = messenger.put('/818 room','CCTV',engineer)
        print("Engineer 1", result)
        timelast = timenow

# b = True
# while b:
#     x = datetime.datetime.now()
#     if True:
#         img = cv2.imread("818_room.png")
#         box,label,count = cv.detect_common_objects(img)
#         count = 0
#         for i in label:
#             if i == 'person':
#                 count += 1
#         print("there are " + str(count) + " people.")
#         engineer = {'Timestamp':x,'People':count}
#         result = messenger.put('/818 room','CCTV',engineer)
#         print("Engineer 1", result)
#     else:
#         print("No image detected. Please! try again")

#     time.sleep(300)

