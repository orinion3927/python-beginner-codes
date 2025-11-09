password=int(input("please create a password: "))
print("are you sure for the password: " ,password)
name=input()
if name == "yes":
    num=int(input("please enter password: "))
    if num == password:
        print("correct password")
    else:
        print("wrong password")
