#Os operadores de identidade são usados para comparar objetos, não se forem iguais, mas se forem realmente o mesmo objeto, com a mesma localização de memória.


string01 = 'Olá Mundão!'
string02 = 'Olá Mundão!'

print(type(string01) is type(string02)) # True
print(type(string01) == type(string02)) # True

