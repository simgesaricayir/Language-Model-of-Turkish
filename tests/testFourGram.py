import NgramModel

fourGram = NgramModel.NgramModel("wiki-data.txt", "test_data.txt",4)
print("size of 4gram: ",fourGram.nGramLen)
print("N1: ",fourGram.N1)
print("Random sentence: ",fourGram.randomSentenceGenerator())
fourGram.calculatePerplexity()