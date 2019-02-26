
def is_even(n):
    ref = {0: True, 1: False}
    return ref[n%2]

def weave(string0, string1):
    final_str = ''
    if len(string0) >= len(string1):
        for i in range(len(string1)):
            final_str += string0[i]+ string1[i]
        final_str += string0[len(string1):]
    else:
        for i in range(len(string0)):
            final_str += string0[i]+ string1[i]
        final_str += string1[len(string0):]
    return final_str

def weave_main(short_str, long_str):
    final_str = ''
    for i in range(len(short_str)):
        final_str += long_str[i]+short_str[i]
    return final_str

def better_weave(str0, str1):
    if len(str0) >= len(str1):
        return weave_main(str1, str0)
    else:
        return weave_main(str0, str1)

def slow_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slow_fib(n-1) + slow_fib(n-2)

def bad_fib(n):
    mem = {0: 0,
           1: 1}
    def f(n):
        if n <= 1:
            return mem[n]
        try:
            mem[n] = mem[n - 1] + mem[n - 2]
            return mem[n]
        except KeyError:
            mem[n] = f(n - 1)
            return f(n - 1) + f(n - 2)
    return f(n)

def better_fib(n):
    # n = int(n)
    # assert type(n) == int, 'input "n" must be and integer'
    mem = {0: 0,
           1: 1}
    def f(n):
        if n <= 1:
            return mem[n]
        try:
            mem[n] = mem[n - 1] + mem[n - 2]
            return mem[n]
        except KeyError:
            mem[n] = f(n - 1)
            return f(n - 1) + f(n - 2)
    return f(n)

def best_fib(n): # ?
    temp = [0, 1]
    for i in range(2, n+1):
        temp1 = temp[0]+temp[1]
        temp[0] = temp[1]
        temp[1] = temp1
    return temp[1]
