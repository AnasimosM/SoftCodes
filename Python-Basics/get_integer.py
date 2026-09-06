# Integer Check

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\t Invalid Choice. Enter an Integer")


def get_string(prompts):
    while True:
        try:
            return str(input(prompts))
        except ValueError:
            print("\t Invalid Choice. Enter a word")
