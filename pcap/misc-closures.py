def greet(text):
    def print_greet() -> None:
        print(text)

    return print_greet


say_hello = greet("helllo")
say_hello()
