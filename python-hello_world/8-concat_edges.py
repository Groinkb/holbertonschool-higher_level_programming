#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
word = str[39:67] + str[107:112] + str[:6]
print(word)
# str[39:67]: Cette expression extrait une sous-chaîne de caractères de la variable str, commençant à l'indice 39 et se terminant juste avant l'indice 67
#str[107:112]: Cette partie extrait une autre sous-chaîne de caractères de la variable str, commençant à l'indice 107 inclus et se terminant à l'indice 112 exclu.
#str[:6]: Cette partie extrait une sous-chaîne de caractères de la variable str, commençant depuis le début de la chaîne (indice 0) jusqu'à l'indice 6 exclu.
