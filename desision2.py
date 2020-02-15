def square_number(number):
    return number * number

number = int(input("Enter number: "))
square = square_number(number)
print("The square is  ", square)   


def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")
    
test_square_number()



#def square(int):
 #   return int * int
#number = int(input("Enter an integer: "))
#print("The square of {} is {}.".format(number, square(number)))