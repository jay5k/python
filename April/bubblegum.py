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
    for duck in [1,2,4,67,8]:
        print(f'{duck} quack')


five()