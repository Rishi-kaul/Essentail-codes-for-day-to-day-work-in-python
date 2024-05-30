import time 
import pyotp
import qrcode


key = pyotp.random_base32()

Name = input("Enter your name :")

totp = pyotp.TOTP(key)
uri = pyotp.totp.TOTP(key).provisioning_uri(name = "Name")

print(uri)

qrcode.make(uri).save("totp.png")

while True :
    print(totp.verify(input("Enter the code :")))


