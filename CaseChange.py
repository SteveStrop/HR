def solve(s):
    words = s.split(" ")

    return  "*"+" ".join(word.capitalize() for word in words)+"*"


if __name__ == '__main__':
    names = ["Chris Allan", "chris allan", "1 allan", "1chris 1allan", "ch1ris all2an" , "132 456 Wq  m e"]
    for test in names:
        print(solve(test))
