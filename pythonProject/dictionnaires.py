def inventaire(offres, objets):

    amis = []

    for element in objets:
        print(element)
        if element in offres:
            amis.append = offres[element]
            #amis.append = offres[element]



    return amis


print(inventaire({"lit" : "Antoine", "bibliothèque" : "Sébastien", "chaise" : "Isabelle",
            "livre 'Le vieil homme et la mer'" : "Ernest", "sac de bonbons" : "Thierry",
            "smartphone" : "Ted", "table" : "Sophie"},
           ["sac de bonbons", "table", "chaise", "lit", "livre 'Le vieil homme et la mer'"]))

