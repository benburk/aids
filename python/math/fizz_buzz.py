def fizzbuzz():
    """No modulo."""
    a = 3
    b = 5
    curr = 0

    for _ in range(20):
        output = ""
        if curr == a:
            output += "Fizz"
            a += 3
        if curr == b:
            output += "Buzz"
            b += 5
        if output == "":
            output = str(curr)
        curr += 1
        print(output)


if __name__ == "__main__":
    fizzbuzz()
