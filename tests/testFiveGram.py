import NgramModel

fiveGram = NgramModel.NgramModel("wiki-data.txt", "test_data.txt",5)
print("size of 5gram: ",fiveGram.nGramLen)
print("N1: ",fiveGram.N1)
print("Random sentence: ",fiveGram.randomSentenceGenerator())
fiveGram.calculatePerplexity()