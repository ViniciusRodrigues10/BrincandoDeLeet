def convertendoFraseParaLeet(frase):
    letras = ["a", "A", "e", "E", "i", "I", "o", "O", "t", "T", "s", "S"]
    letrasLeet = ["@", "@", "3", "3", "1", "1", "0", "0", "7", "7", "5", "5"]
    fraseLeet = ""
    quantSubstituicoes = 0
    for i in frase:
        if i in letras:
            i = letrasLeet[letras.index(i)]
            quantSubstituicoes += 1
        fraseLeet += i
    return fraseLeet[::-1], quantSubstituicoes

frase = str(input()).strip()
if frase == '':
  print("0")
elif frase.isalpha() == False:
  print("numeros\n0")
else:
    for i in convertendoFraseParaLeet(frase):
        print(i)
