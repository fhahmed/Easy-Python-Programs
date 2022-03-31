#Program_to_check_primality_of_a_number
def prime(num):
    if num<=1:
        return("It is not a prime number.")
    for i in range(2,num):
        if num%i==0:
            return("It is not a prime number.")
            break
    return("It is a prime number.")
ch=int(input("Enter the number:"))
print(prime(ch))
