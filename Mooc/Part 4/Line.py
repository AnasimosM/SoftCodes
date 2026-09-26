def line(amount:int,word:str):
    
    if word == "":
        word = "*"

    print(word[0] * amount)

if __name__ == "__main__":
    line(3, "%")
