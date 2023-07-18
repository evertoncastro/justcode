

def factorial(value):
    if value == 1:
        return value
    return factorial(value-1) * value


if __name__ == "__main__":
    print(factorial(5))