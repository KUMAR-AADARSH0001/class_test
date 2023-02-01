class Reverse:
    var = 'hello .py'
    print(var)
    split = var.split(" ")
    for i in split[::-1]:
        print(i, end=' ')


Reverse()
