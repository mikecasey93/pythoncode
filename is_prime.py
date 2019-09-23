def is_prime(num):

    condition = True

    for i in range(2, num):

        if num % i != 0:

            condition = True

        else:
            condition = False
            break

    return condition

print(is_prime(11))
    
