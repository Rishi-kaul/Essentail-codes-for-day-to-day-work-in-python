import time
import pyotp

key = pyotp.random_base32()

counter = 0

hotp = pyotp.HOTP(key)
print(hotp.at(0,5000))
for i in range(5000):
    print(hotp.verify(input("Enter the code:"),counter)) 
    counter += 1
