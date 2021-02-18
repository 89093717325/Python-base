sum = 0
for i in range (1000, 20001):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
        sum += i
    elif (i % 3 == 0):
        print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)
print(sum)