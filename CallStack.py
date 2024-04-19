def funOne():
    funTwo()
    print("1")

def funTwo():
    funThree()
    print("2")

def funThree():
    print("3")
    

funOne()