# This project improves your skill issue (...)

from project import foo, bar, magic

@magic
def is_odd(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_odd(n - 1) < is_odd(n - 2)
