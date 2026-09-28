words = []

while True:
    get_words = str(input("Word: "))

    if get_words in words:
        print(f"You typed in {len(words)} different words")
        break
    words.append(get_words)
