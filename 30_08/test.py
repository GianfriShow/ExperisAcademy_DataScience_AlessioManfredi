# 5
# take as input a word and add it to a list, ask if the user wants to repeat this by adding another word, then print all elements in the list at the end

def print_list():

    # preparation and first input
    sequence = []
    word = input("Please type a string to add to your list:    ")
    keep_going = True
    sequence.append(word)
    
    # core loop
    while keep_going:
        word = input("Type another string if you want to keep going, otherwise press 'Enter' if you want to print your current list:    ")
        if word == '':
            keep_going = False
        else:
            sequence.append(word)

    # print final output
    print("Here's your list:\n")
    for element in sequence:
        print(element)

print_list()

# 7
'''
Le tre regole fondamentali dell'OOP sono incapsulamento, ereditarieta', e polimorfismo:
l'incapsulamento si riferisce alla capacita' di poter nascondere certi aspetti/elementi degli oggetti che non vogliamo far trapelare,
o al contrario di mostrare cio' che desideriamo rivelare;
l'ereditarieta' e' la possibilita' di assegnare a vari oggetti le caratteristiche specifiche di un'altra classe gia' esistente, permettendo
in questo modo di creare delle gerarchie o alberi genealogici con relazioni di parent-child;
il polimorfismo e' strettamente collegato all'ereditarieta' in quanto e' l'abilita' di cambiare forma di un oggetto ma non il comportamento,
o al contrario di cambiare il comportamento ma non la forma, permettendoci di trattare oggetti di classi diverse allo stesso modo fintanto che abbiano
una classe in comune (stesso parent).
Per quanto riguarda l'astrazione, il concetto sembra simile all'incapsulamento, perche' ci da' la possibilita' di offuscare gli elementi complicati
o non necessari, confusionali, per mostrare invece soltanto le parti rilevanti e di interesse; l'astrazione favorisce la semplicita' e l'intuitivita',
due concetti fondamentali e alla base di un linguaggio high-level come Python, che invece di comunicare con la macchina direttamente attraverso
un insieme di 0 e 1, utilizza un interprete per verificare e compilare lo script prima di eseguirlo, astraendo questi passaggi al programmatore e cosi'
aumentando il livello di semplicita' di approccio del linguaggio.
'''