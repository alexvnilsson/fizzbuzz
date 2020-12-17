n_max = 100

n_fizz = 3
n_buzz = 5

n_printable = {
    3: "Fizz",
    5: "Buzz",
    15: "FizzBuzz"
}

def get_printable(n):
    if n_printable[n] == None:
        raise Exception(f"Saknar utskrivbar repr. av numret {n}.")

    return n_printable[n]

def is_divisible(n, by_n):
    n_sum = (n / by_n)

    if type(n_sum) is float:
        return n_sum.is_integer()

    if type(n_sum) is int:
        return True

    return False

def is_fizzbuzz(n) -> int:
    n_test = (n_fizz, n_buzz, (n_fizz * n_buzz))
    n_sum = 0

    for n2 in n_test:
        if is_divisible(n, n2):
            n_sum = n2
    
    return n_sum


for n in range(1, (n_max + 1)):
    n_result = is_fizzbuzz(n)

    if n_result == 0:
        print(n)
    else:
        try:
            print(get_printable(n_result))
        except Exception:
            print(n)
