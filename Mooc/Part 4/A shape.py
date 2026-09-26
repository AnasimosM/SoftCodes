def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)
    
def shape(base:int,triangle:str,height:int,rectangle:str):
    count = 1
    while count <= base:
        line(count,triangle)
        count += 1
    while count - 1 == base and height > 0:
        line(count-1,rectangle)
        height -= 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")
