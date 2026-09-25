def squared(text, size):
    count = 0
    row = ""
    while count < (size * size): 
        if count > 0 and count % size == 0:
            print(row)
            row = ""
        row += text[count % len(text)]
        count += 1
    print(row)


if __name__ == "__main__":
    squared("ab",5)
