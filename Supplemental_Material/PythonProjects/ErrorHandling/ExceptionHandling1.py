
while True:
    try:
        age = int(input("enter your age: "))
        if age < 18:
            print("welcome, Kiddo!!")
            break
        else: 
            print("Howdy, Sir!")
            break
    except ValueError:
        print("please enter numeric age")

