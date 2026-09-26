def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)

   
def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

if __name__ == "__main__":
    box_of_hashes(5)
