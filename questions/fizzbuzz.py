# loop 100 times
# print fizz if its divisible by 3
# print buzz if its divisible by 5
# print fizzbuzz if its divisible by 3 and 5


for i in range(1,101):
    str = ""
    if i % 3 == 0:
        str += "Fizz"
    if i % 5 == 0:
        str += "Buzz"
    if str:
        print(i, str)


l = [1,2,3,4,45,4]

print(l[-2:])