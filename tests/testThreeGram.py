import NgramModel

threeGram = NgramModel.NgramModel("wiki-data.txt", "test_data.txt",3)
print("size of 3gram: ",threeGram.nGramLen)
print("N1: ",threeGram.N1)
print("Random sentence: ",threeGram.randomSentenceGenerator())
threeGram.calculatePerplexity()