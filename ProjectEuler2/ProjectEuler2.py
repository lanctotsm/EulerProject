
sum = 0
fib = 1
prev = 0
while True:
    if fib %2== 0:
        sum += fib
    temp = fib
    fib = prev + fib
    prev = temp
    if fib > 4000000:
        break;

print(sum)