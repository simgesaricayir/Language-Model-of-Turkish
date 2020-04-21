import NgramModel

oneGram = NgramModel.NgramModel("wiki-data.txt", "test_data.txt",1)
print("size of 1gram: ",oneGram.nGramLen)
print("N1: ",oneGram.N1)
print("Random sentence: ",oneGram.randomSentenceGenerator())
oneGram.calculatePerplexity()

