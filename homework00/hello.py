def get_greeting(name: str) -> str:
    return_string = "Hello, " + name + "!"
    return return_string


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
