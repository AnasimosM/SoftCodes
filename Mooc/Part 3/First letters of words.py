# word = str(input("Please type in a sentence: "))
# while word in word.split():
#     print(word[0])

# sentence = "Aa Bb Cc"             #str(input("Please type in a sentence: "))
# while True:
#     count = sentence.find(" ")
#     print(f"Count: {count}")
#     if count == -1:
#         print(f"{sentence[0]}")
#         break
#     while count < len(sentence):
#         print(f"{sentence[count:count+2]}")
#         count += 1
#     break
#
# count = sentence.find(" ")
# print(f"Count: {count}")
# print(f"Sentence: {len(sentence)} Index is {len(sentence)-1}")
# print(f"Letter : {sentence[count]}")


# for word in input("Please type in a sentence: ").split():
#     print(word[0])


words = str(input("Please type in a sentence: "))
count = 0
while count < len(words.split()):
    first = words.split()
    print(first[count][0])
    count += 1

