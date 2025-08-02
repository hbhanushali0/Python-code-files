#wapp to read twofiles and find the similarity
import spacy
nlp = spacy.load("en_core_web_lg")

#read the data of two files
f1 = input("enter first file name ")
f = open(f1,"r")
d1 = f.read()
f.close()

f2 = input("enter second file name ")
f = open(f2, "r")
d2 = f.read()
f.close()

#vectorize the data
vd1 = nlp(d1)

vd2 = nlp(d2)


#find similarity
simi = vd1.similarity(vd2)
print(round(simi * 100, 2), "%")

