"""
Word occurrences
"""

word_to_frequency = {}
sentence = input("Enter a sentence: ")
sentence_set = sentence.split(" ")
for word in sentence_set:
    frequency = word_to_frequency.get(word, 0)
    word_to_frequency[word] = frequency + 1
words = list(word_to_frequency.keys())
words.sort()
longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, word_to_frequency[word]))
