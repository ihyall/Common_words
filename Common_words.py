import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer

text = open(r'Уэллс_-_Война_миров.txt').read()

d = {}
for word in RegexpTokenizer("[аАaA-яЯёЁzZ]+").tokenize(' '.join(text.lower().split())):
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

d_word_sorted = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}

print('Количество строк:', text.count("\n")+1)
print(f'Количество слов: {sum(list(d_word_sorted.values()))}')
print(f'Количество символов с пробелами: {len(text)}')
print(f'Количество символов без пробелов: {len(text.replace(" ", ""))}')

plt.bar(list(d_word_sorted.keys())[:20], list(d_word_sorted.values())[:20])
plt.show()