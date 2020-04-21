import NgramModel

twoGram = NgramModel.NgramModel("wiki-data.txt", "test_data.txt",2)
print("size of 2gram: ",twoGram.nGramLen)
print("N1: ",twoGram.N1)
print("Random sentence: ",twoGram.randomSentenceGenerator())
twoGram.calculatePerplexity()