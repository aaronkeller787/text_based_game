from time import sleep

def print_slow(str):
    for l in str:
        sleep(.05)
        print(l, end='', flush=True)


