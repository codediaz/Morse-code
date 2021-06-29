
print(" "*76)
print("="*76)
print(" "*20 + " Universidad Politécnica Salesiana ")
print(" "*30 + " Código Morse ")
print("="*76)
print( "Bienvenido!, a continuación transformare una palabra o frase en código morse. ")
print(" "*76)   
    
codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}

def morse_txt():
    txt_codificado= ""

    palabra = input("     Ingrese una palabra o texto a codificar: ")

    for c in palabra:
        if c != " " and c.lower() in codigo_morse:
            txt_codificado+= codigo_morse[c.lower()]
        else:
            txt_codificado+= c
    print(" ")   
    print("     Texto codificado: {}".format(txt_codificado))
    
def despedida():
    print(" ")
    print(" "*5+"+--------------------------------------+")

    print(" "*5+ "| Gracias por utilizarme, hasta luego! |") 

    print(" "*5+"+--------------------------------------+") 
    
    print(" ")
    
morse_txt()
despedida()    