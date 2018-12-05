def greet_mark():
    print("Hallo Mark")
    print("We have 6 apples in stock.")


def greet_brooke():
    print("Hallo Brooke")
    print("We have 6 apples in stock.")


def greet_jane():
    print("Hallo Jane")
    print("We have 6 apples in stock.")


greet_brooke()
greet_jane()
greet_mark()

def greet_customer(name, num_apples=19):
    print("Hallo, " + name)
    print("We have " + str (num_apples) + " " + "apples in stock.")

greet_customer("Mark")
greet_customer("Jane" , 6)
greet_customer("Brooke" , 5)

