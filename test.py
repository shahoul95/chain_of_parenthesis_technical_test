# -*- coding: utf-8 -*-

def test_chain(parenthesis_str):
    """
    Vérifie si une chaîne de parenthèses est bien formée.

    Args:
    - parenthesis_str (str): La chaîne de parenthèses à vérifier.

    Returns:
    - bool: True si la chaîne est bien formée, False sinon.
    """
    stack = []

    for char in parenthesis_str:
        if char == '(':
            stack.append('(')
        elif char == ')':
            # Si la pile est vide, la chaîne est mal formée.
            if not stack:
                return False
            # Sinon, retirer une parenthèse ouvrante de la pile.
            stack.pop()

    # Si la pile est vide à la fin, la chaîne est bien formée.
    return len(stack) == 0


parenthesis_str_1 = "()((()))(()((((()()()()))))()()()))))))()()())))()()(()"
result_1 = test_chain(parenthesis_str_1)
print("La chaîne est bien formée : {}".format(result_1))


def find_wellformed_subchain(parenthesis_str):
    """
    Trouve la taille de la plus longue sous-chaîne bien formée.

    Args:
    - parenthesis_str (str): La chaîne de parenthèses à analyser.

    Returns:
    - int: La taille de la plus longue sous-chaîne bien formée.
    """
    max_length = 0
    stack = [-1]  # Utiliser -1 comme indice de départ dans la pile.

    for i in range(len(parenthesis_str)):
        if parenthesis_str[i] == '(':
            # Ajouter l'indice de la parenthèse ouvrante à la pile.
            stack.append(i)
        else:
            if stack:
                # Retirer l'indice de la parenthèse ouvrante associée.
                stack.pop()
                if not stack:
                    # Si la pile est vide, ajouter l'indice actuel à la pile.
                    stack.append(i)
                else:
                    # Calculer la taille de la sous-chaîne bien formée.
                    max_length = max(max_length, i - stack[-1])
            else:
                # Ajouter l'indice actuel à la pile si la pile est vide.
                stack.append(i)

    return max_length


parenthesis_str_2 = "()((()))(()((((()()()()))))()()()))))))()()())))()()(()"
result_2 = find_wellformed_subchain(parenthesis_str_2)
print("La taille de la plus longue sous-chaîne bien formée est : {}".format(result_2))
