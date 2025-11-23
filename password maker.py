password=int(input("please create a password: "))
print("are you sure you wanna save the password: " ,password)
name=input()
if name == "yes":
    num=int(input("please enter password: "))
    if num == password:
        print("correct password")
    else:
        print("wrong password")
# do not copy this code or other codes from the repository "python beginner codes". (in github)
