# Seja o mesmo texto acima “splitado”.
# Calcule quantas palavras possuem uma das letras“python”
# e que tenham mais de 4 caracteres.
# Não se esqueça de transformar maiúsculas para minúsculas
# e de remover antes os caracteres especiais

import string

def isPython(word):
  for index in word:
    if index in 'python':
      return True
  return False

text = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower()
list = []

for i in string.punctuation:
    text = text.replace(i, ' ')


for i in text.split():
    if isPython(i) and len(i) > 4:
        list.append(i)

print(list)
print(len(list))
