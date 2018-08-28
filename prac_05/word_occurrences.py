words = {}
sentence = input("Enter a sentence: ")
sentence_set = sentence.split(" ")
for word in sentence_set:
    word_frequency = words.get(word, 0)
    words[word] = word_frequency + 1
print(sentence_set)
print(words)