# Gere uma lista de palavras deste texto com
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
# e cuidado com maiúsculas e minúsculas.

import string
text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, andwhatever your background, we welcome you'.lower()
for i in string.punctuation:
    text = text.replace(i, ' ')

list = []
for i in text.split():
    if i[0] in 'python' or i[-1] in 'pyton':
        list.append(i)

print(list)
