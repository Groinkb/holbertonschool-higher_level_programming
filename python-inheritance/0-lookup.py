def lookup(obj):
    return [attr for attr in dir(obj)]

# Exemple d'utilisation :
result = lookup("Bonjour, le monde !")
for item in result:
    print(item)
