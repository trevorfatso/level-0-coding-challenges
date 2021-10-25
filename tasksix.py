#task6
def maximum(*args):
    benchmark = 0
    for i in args:
        if i > benchmark:
            benchmark = i
    print(f'{benchmark}')