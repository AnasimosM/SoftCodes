def same_chars(text:str,index1,index2):
    while index1 <= (len(text) - 1) and index2 <= (len(text) - 1):
        if text[index1] == text[index2]:
            return True
        return False
    return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))

    # def same_chars(str, a, b):
    # if a >= len(str) or b >= len(str):
    #     return False
    # return str[a] == str[b]
