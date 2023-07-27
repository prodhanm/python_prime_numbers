import sys

n = 250

def nums():
    nums_list = [num for num in range(1,n)]
    return nums_list

def main():
    print(nums())

if __name__ == "__main__":
    main()