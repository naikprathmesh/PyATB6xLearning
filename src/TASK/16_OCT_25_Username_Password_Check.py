# Check if the user can log in based on correct username and password.
#
# I/p
#
# username = "admin"
# password = "1234"
#
# O/p
# ✅ Login Successful
#
#
# For the Fail condition Other O/P = ❌ Invalid Credentials

username = str(input("Enter Username: "))
password = str(input("Enter Password: "))

if username.strip() == "admin" and password.strip() == "1234":
    print("Login Successful")
else:
    print("Login Failed")