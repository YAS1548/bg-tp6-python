# Les données : une liste (slide 26) et tuples (slide 28)
# tuple = (matricule, nom, prénom, note, autre valeur)
students = [
 # Ici on crée une liste (vu dans le slide 26) et on l'affecte à la variable students (slide 23)
    (1000, "JOHN", "DOE", 14,5), 
    (2000,  "BOB", "CARLTON", 7, 1), 
    (3000, "RAYANE", "SMITH", 13, 3), 
]

# Fonction B
def B(moyenne: float) -> bool:# Déclaration d'une fonction 
                           #avec paramètre et typage (slides 40 et 41)
    return moyenne >= 10 # Opérateur rationnel >= (slide 34) : True si la note est au moins 10,
                      # sinon False (booléen, slide 24)


# Fonction A
def A(students: list) -> list:  # Fonction avec un paramètre de type list (slides 40 et 41)

    resultats = [] # On crée une liste vide pour stocker les résultats (slide 26)

    for etudiant in students: # Boucle for : on parcourt chaque tuple de la liste (slide 38)

         mat  = etudiant[0] # On lit le matricule avec son index 0 (accès à un tuple, slide 28)

         note1 = etudiant[3]
         note2 = etudiant[4]

         moyenne = (note1 + note2) / 2  # Opérateurs arithmétiques + et / (slide 34) : moyenne des deux notes
         
         if B(float(moyenne)): # Condition if (slide 35) : on appelle B avec la note convertie en float

             decision = "ADMIS"

    
         else:  # Sinon (else, slide 35)
             decision = "AJOURNE"

         resultats.append({"mat": mat, "result": decision}) # Dictionnaire clé:valeur (slide 31) ajouté à la liste avec append (slide 27)

    return resultats   # On retourne la liste de dictionnaires, c'est-à-dire le résultat JSON (slide 33)

# Fonction C
def C(): # Fonction sans paramètre (slide 40)
    resultats = A(students)  # Appel de la fonction A avec la liste students (slide 40)
    for r in resultats:  # Boucle for sur la liste de dictionnaires (slides 32 et 38)
        print(f"{r['mat']}: {r['result']}") 

# Point d'entrée du programme (slide 55)
if __name__ == "__main__":  # Ce bloc ne s'exécute que si on lance directement le fichier (slide 55)
    C()  # On appelle la fonction C pour afficher les résultats
         
          