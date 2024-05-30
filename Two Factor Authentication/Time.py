# time based OTP
import  time
import pyotp

key = pyotp.random_base32()

toptp = pyotp.TOTP(key) 

int_code = input("Enter 2FA Code :")

code = toptp.now()

# using verification  to verify the otp for at that point 

print(toptp.verify(int_code))



"""print(toptp.now())

time.sleep(30)

print(toptp.now())"""

# print(key)