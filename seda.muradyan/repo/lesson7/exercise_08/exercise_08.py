
def next_prime(n):
    number = n + 1
    #We know that we will find a prime so this loop can be endless
    while True:
        if (number):
            return number
        number += 1
         
def main():
    n = input("Find the first prime larger than (Enter a number): ")
    n = int(n)
    print(next_prime(n))
     
if __name__ == '__main__':
    main()