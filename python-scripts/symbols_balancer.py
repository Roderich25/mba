def main():
    texto = ""
    with open("texto.txt") as archivo:
        for linea in archivo:
            texto += linea
    print('*'*150)
    print(texto)
    print('*'*150)

    print(checa_balanceo(texto))


def checa_balanceo(texto):
    pila = []  # Make an empty stack.
    simbolos_apertura = ['{', '[', '(']  # opening symbols
    simbolos_clausura = ['}', ']', ')']  # closing symbols
    for caracter in texto:  # Read characters until end of file.
        if caracter in simbolos_apertura:
            # If the character is an opening symbol, push it onto the stack.
            pila.append(caracter)
        if caracter in simbolos_clausura:
            if len(pila) == 0:
                # If it is a closing simbol and the the stack is empty, report an error.
                return "Error"
            else:
                c = pila.pop()  # Otherwise, pop the stack .
                # If the symbol popped is not the corresponding opening symbol, then report an error.
                if c == '{' and caracter != '}':
                    return "Error"
                if c == '[' and caracter != ']':
                    return "Error"
                if c == '(' and caracter != ')':
                    return "Error"
    # At end of file, if the stack is not empty, report an error.
    if len(pila) == 0:
        return "Balanced!\n"
    else:
        return "Error"


if __name__ == '__main__':
    main()
