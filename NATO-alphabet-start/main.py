import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Say a word\n").upper()

result = [phonetic_dic[letter] for letter in word]
print(result)
