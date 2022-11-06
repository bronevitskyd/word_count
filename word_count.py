texte = input("Ecrivez un texte ici et je vous dirais le nombre de mots: ") #


def word_count():    ##retourne le mots
    word_count =(len(texte.split()))
    return word_count


print("Voici votre nombre de mots: ")  #print le nombre de mots
print(word_count())

