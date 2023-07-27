import sys

def prime_nums(nums):
    prime = True
    for num in range(2,21):
        if nums%nums == 0:
            prime = False
    if prime:
        print(f"{nums} is prime.")
    else:
        print(f"{nums} is not prime")

def main():
    return prime_nums(3)

if __name__ == "__main__":
    main()