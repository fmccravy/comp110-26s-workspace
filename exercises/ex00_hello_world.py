"""My first exercise in COMP110!"""

__author__ = "730941956"


def greet(name: str) -> str:
    return "Hello, " + name + "!"


greet(name="student")
greet(name="Faith")
greet("f" + "ait" + "h")
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
