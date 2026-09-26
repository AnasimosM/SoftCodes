def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)

def square_of_hashes(size):
    length = size
    while size > 0:        
        line(length, "#")
        size -= 1

if __name__ == "__main__":
    square_of_hashes(3)
