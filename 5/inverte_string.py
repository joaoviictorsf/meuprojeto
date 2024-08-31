def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

def main():
    entrada_usuario = input("Digite a string a ser invertida: ")
    
    string_invertida = inverter_string(entrada_usuario)
    
    print(f"String original: {entrada_usuario}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
