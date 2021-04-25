cats = ['rocket', 'maverick', 'sebastian']

for index, cat in enumerate(cats):
    print(f"{index} {cat} cats[index] = {cats[index]}")


def test():
    return "taco", "cat"


def one():
    ret = test()
    print(ret)


def two():
    taco, cat = "taco", "cat"
    print(f"{taco}, {cat}")


def three():
    taco, cat = test()
    print(f"{taco}, {cat}")


def four():
    t, taco, cat = test()
    print('hello')


def five():
    for duck in [1, 2, 4, 67, 8]:
        print(f'{duck} quack')


five()

def question():
    while True:
        try:
            age = int(input("what is your age? >"))
        except ValueError:#only if this exception is thrown
            print("Please enter a number")
            continue
        if age == 21:
            print("welcome back")
            break

question()

a = "cats dog".upper()
print(a)
a = "cats dog".upper().lower()
print(a)


