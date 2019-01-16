def drink():
    age = int(input("How old are you? "))
    if age >= 21:
        print("This guy can drink.")
    else:
        print("This guy can't drink because he's " + age + " years old.")

drink()