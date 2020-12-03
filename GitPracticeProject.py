# GitPracticeProject.Py

# Practice project to demonstrate Git workflow

def main():
    # find the nth Fibonacci number
    # e.g. 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    n = int(input("What Fibonacci number do you want to find? "))

    if n in [1, 2]:
        print(f"The {n}st/nd Fib number is 1. ")


if __name__ == "__main__":
    main()
