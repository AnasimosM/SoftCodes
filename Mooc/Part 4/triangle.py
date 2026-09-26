def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)

def triangle(size):
    length = 1
    while length <= size:        
        line(length, "#")
        length += 1

if __name__ == "__main__":
    triangle(5)
