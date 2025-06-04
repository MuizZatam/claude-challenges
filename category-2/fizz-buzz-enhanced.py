from math import sqrt

# Note: apply concepts in hint later down
for i in range(1, 101):

    prime = True

    for j in range(2, round(sqrt(i)) + 1):

        if i % j == 0:

            prime = False
            break

    if i % 3 == 0:

        print("Prime Fizz" if prime else "Fizz")

    elif i % 5 == 0:

        print("Prime Buzz" if prime else "Buzz")

    elif i % 3 == 0 and i % 5 == 0:

        print("Prime FizzBuzz" if prime else "FizzBuzz")

    else:

        print(f"Prime {i}" if prime else i)