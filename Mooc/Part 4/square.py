def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)

def square(size, character):
    length = size
    while size > 0:        
        line(length, character)
        size -= 1

if __name__ == "__main__":
    square(5, "x")
