# def fizzbuzz(name, age):
#     print("hello " + name + ", you are " + str(age))
#
# fizzbuzz("mike", 35)
#
# def cube(num):
#     return num*num*num
#     print("cod")
# result = cube(4)
# print(result)

class Fizzbuzz:
    def __init__(self, num):

        self.num = num

    def isdivisible(self):
        if self.num % 15 == 0:
          return "FizzBuzz"
        elif self.num % 5 == 0:
          return "Buzz"
        elif self.num % 3 == 0:
          return "Fizz"
        else:
          return self.num
p1 = Fizzbuzz(78)
print(p1.isdivisible())