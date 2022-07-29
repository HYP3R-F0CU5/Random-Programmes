
def solo():
    pass



def mult(word):
    word = list(word)
    
    return word



a = int(input("1.Solo \nor \n2.multiplayer\n\n>"))
while a != 1 and a != 2:
    print("Please choose either options 1 or 2.")
    a = int(input("1.Solo \nor \n2.multiplayer\n\n>"))
if a == 2:
    input("Please let player 2 choose a word between 1-20 characters long\n>")
    while len(word) > 21 or len(word) < 1:
        print("That is not within the word limit")
        word = input("Please let player 2 choose a word between 1-20 characters long\n>")
    print(mult(word))
