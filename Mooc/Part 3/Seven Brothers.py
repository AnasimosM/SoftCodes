def seven_brothers():
  name = ["Eero","Aapo","Juhani","Lauri","Simeoni","Timo","Tuomas"]
  count = 0
  while count <= len(name) - 1:

    name.sort()
    print(name[count])
    count += 1
 
if __name__ == "__main__":
  seven_brothers()
