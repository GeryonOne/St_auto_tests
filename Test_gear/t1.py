def greet(name: str = None):
    if name is None:
        print("Hello, anonymous!")
    else:
        print(f"Hello, {name}!")


greet("Victor")
greet()