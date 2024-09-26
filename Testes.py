frase = 'Lauren ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat'
print(len(frase))
i = 0

while i < len(frase):
    letra_atual = frase[i]
    qnt = frase.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue
    print(letra_atual, qnt)
    i += 1