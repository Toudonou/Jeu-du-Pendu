import random

WORDLIST = ["ado", "bis", "glu", "hop", "mai", "tic", "ardu", "taux", "banjo", "escot", "moult", "faucon", "sadord", "yankee", "bonjour", "revoir"]
play = 1

while play == 1:
    word = WORDLIST[random.randint(0, len(WORDLIST) - 1)]
    nbrCoups = int(len(word) * 1.5)  # int(5.2) -> 5, int("7855") -> 7855
    hideWord = []
    win = False

    for i in word:
        hideWord.append("*")

    while nbrCoups:
        badLetter = True
        print("Squelette du mot : " +  "".join(hideWord).upper()) # "-".join(["4", "e", "fdvdf"]) -> "4-e-fdvdf"
        print("Nombre de coups restant : " + str(nbrCoups)) # str(475) -> "475"
        entrer = input("Entrer une lettre : ")
        for i in range(len(word)):
            if entrer == word[i]:
                hideWord[i] = entrer
                badLetter = False
                break
        
        if badLetter:
            print("Vous avez entré une mauvaise lettre")
        
        if "".join(hideWord) == word:
            win = True
            break
        
        nbrCoups -= 1
        if nbrCoups == 0:
            win = False
            break

        print("")

    if win:
        print("\nFELICITATION !!!\n")
    else:
        print("\nPERDU\n")
    
    play = int(input("Play again (1 pour oui, 2 pour non) : "))
    print("")

print("AU REVOIR...")
