## TEST

Fonction test_chain :

La fonction test_chain prend en entrée une chaîne composée de parenthèses et vérifie si les parenthèses sont bien formées.

Elle utilise une pile pour suivre les parenthèses ouvrantes et s'assure que chaque parenthèse fermante a une parenthèse ouvrante correspondante.

La complexité temporelle de cette fonction est O(n), où n est la longueur de la chaîne d'entrée, car elle parcourt la chaîne une fois.

La complexité mémoire est O(m), où m est la taille maximale de la pile pendant l'itération.

Fonction find_wellformed_subchain :

La fonction find_wellformed_subchain trouve la taille de la plus longue sous-chaîne bien formée dans une chaîne composée de parenthèses.

Elle utilise une pile pour suivre les indices des parenthèses ouvrantes et calcule la longueur des sous-chaînes bien formées.

La complexité temporelle de cette fonction est O(n), où n est la longueur de la chaîne d'entrée, car elle parcourt la chaîne une fois.

La complexité mémoire est O(k), où k est la taille maximale de la pile pendant l'itération.

## USAGE

Fonction test_chain

parenthesis_str_1 = "()((()))(()((((()()()()))))()()()))))))()()())))()()(()"
result_1 = test_chain(parenthesis_str_1)
print("La chaîne est bien formée : {}".format(result_1))

Fonction find_wellformed_subchain

parenthesis_str_2 = "()((()))(()((((()()()()))))()()()))))))()()())))()()(()"
result_2 = find_wellformed_subchain(parenthesis_str_2)
print("La taille de la plus longue sous-chaîne bien formée est : {}".format(result_2))




