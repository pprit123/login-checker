def check_password(pw):
    if pw == "Life":
        return True
    else:
        return False
for attempts in range(3):
    tries = input("Enter the password: ")
    if check_password(tries):
        print("Login Successful.")
        break
    else:
        print("Failed Login.")
else:
    print("Account deactivated.")
