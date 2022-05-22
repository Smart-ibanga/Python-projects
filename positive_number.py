user_no = input("Enter a number: ")

try:
    user_no = int(user_no)
    print("Hooray you entered a number")


    if user_no >= 0 :
        print("True")

    else:
        print("False")


except:
    print("This is not a number")
