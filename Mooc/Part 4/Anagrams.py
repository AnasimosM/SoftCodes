def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False

# def anagrams(word1:str,word2:str):
#     sortedword1 = list(sorted(word1))
#     sortedword2 = list(sorted(word2))
#     if sortedword1 == sortedword2:
#         return True
#     return False
