#! Python 3

# This code will find the largest prime factor of a given number

print('Please input the number you would like the largest prime factor of')
x = int(input())

def MaxFactor(Number):
    for i in range(1, Number-1):
        if Number % i == 0:
            for j in range(i-1, 0, -1):
                if j == 1:
                    print(i)
                elif i % j == 0:
                    break

print(MaxFactor(x))
print('done')
