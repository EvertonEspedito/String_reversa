def inverter_string(s):
    # Convertendo a string para uma lista de caracteres
    caracteres = list(s)
    
    # Invertendo a lista de caracteres
    tamanho = len(caracteres)
    for i in range(tamanho // 2):
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]
    
    # Construindo a string invertida a partir da lista de caracteres
    string_invertida = ''.join(caracteres)
    
    return string_invertida

# Exemplo de uso
string_original = "Exemplo"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)

