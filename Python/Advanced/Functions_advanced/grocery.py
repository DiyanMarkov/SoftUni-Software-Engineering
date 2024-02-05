def grocery_store(**kwargs):
    #bread = 2

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join([f"{p}: {q}"for p, q in kwargs])

print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))
