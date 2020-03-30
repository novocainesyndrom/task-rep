from functools import reduce

class Operations:
    def __init__(self, number):
        self.number = number

    def is_divisible_by(self, divisor):
        return self.number % divisor == 0

    @staticmethod
    def multiply(val_1, val_2):
        return (lambda : val_1 * val_2)()

    def __del__(self):
        print("Goodnight, sweet prince")

class Private(Operations):

    __var = "I'm protected variable"
    def _is_string(self):
        return type(str()) == type(self.number)

class Common_Operations(Private):

    @staticmethod
    def multiply(val_1, val_2):
        gcd = lambda val_1, val_2: abs(val_1) if val_2 == 0 else gcd(val_2, val_1 % val_2)
        gcd = gcd(val_1, val_2)
        lcm = (val_1 * val_2)/gcd
        return gcd, lcm

if __name__ == "__main__":
    obj = Operations(15)
    div = 3
    print(f"{obj.number} divisible by {div} " if obj.is_divisible_by(3) else f"{obj.number} not divisible by {div} " )
    nums = 16, 20
    print("{0} * {1} = {2}".format(*nums, obj.multiply(*nums)))
    del obj

    obj2 = Private(61)
    print(f"{obj2.number} divisible by {div} " if obj2.is_divisible_by(3) else f"{obj2.number} not divisible by {div} ")
    print(f"{obj2.number} is string " if obj2._is_string() else f"{obj2.number} not string ")
    try:
        obj2.__var
    except:
        print("Something went wrong")
    print(obj2._Private__var)
    
    obj3 = Common_Operations(5)
    print("GCD = {0}; LCM = {1}".format(*obj3.multiply(*nums)))

    # Use map to print the square of each numbers rounded
    # to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    # Fix all three respectively.
    map_result = list(map(lambda x: round(pow(x, 2),2), my_floats))
    filter_result = list(filter(lambda name: len(name)<=7 , my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)
