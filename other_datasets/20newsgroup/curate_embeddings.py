import pickle
import gensim,pdb
import numpy as np
#words_set = pickle.load(open("word_set.pkl","r"))

words_set = []
both_files = ["20ng-train-no-stop.txt","20ng-test-no-stop.txt"]
for each_file in both_files:
    f = open(each_file,"r").readlines()
    for line in f:
        each_class, doc = line.split("\t")
        words_set.extend(doc[:-1].split())

words_set = set(words_set)



model = gensim.models.KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin', binary=True)

#pdb.set_trace()

model_part = {}
for word in words_set:
    if(word in model):
        model_part[word] = model[word]


print len(model_part)

pickle.dump(model_part,open("word_embedding_dict.pkl","w"))