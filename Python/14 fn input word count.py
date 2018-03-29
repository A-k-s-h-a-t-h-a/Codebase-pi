def time(sent, words):
    return (words, "occurs", sent.count(words), "times")

sent = input('Enter a sentence')
words = input('Enter word')

print(time(sent, words))