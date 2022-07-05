

def square_root(Xo, a, diff):
    """ 
    It determines the square root of a number.
    Where Xo is the initial value, a is the number and
    diff is the approximation value
    """
    assert Xo > 0, print("inital is no valid")
    assert diff > 0, print("The approximation value is not valid for the calculation")
    count = 0
    while diff > 0.000000001:
        x = 0.5 * (Xo + a / Xo)
        Xo = x
        diff = abs(a - (x * x))
        count += 1
    print(f"The number of time of iteration is {count}")
    return round(x, 4)


def print_number():
    Xo = int(input("Enter the initial number: "))
    a = int(input("Enter the value of the number: "))
    diff = float(input("Enter the approximation value: "))
    x = square_root(Xo, a, diff)
    print(f"The square root of {a} is {x}")

print_number()
