import re

class TextAnalyzer(object):
    def __init__(self, text):
        formatedText = re.sub("[^0-9a-zA-Z ]", "", text)
        formatedText = formatedText.lower()
        self.text = formatedText

    def freqAll(self):
        words = self.text.split(" ")
        freq = {}

        for ele in set(words):
            freq[ele] = words.count(ele)

        return freq
    
    def freqOf(self, word):
        freq_all = self.freqAll()

        if(word in freq_all):
            return freq_all[word]
        else:
            return 0

obj = TextAnalyzer("Hello , how are you?")
print(obj.text, obj.freqAll())
