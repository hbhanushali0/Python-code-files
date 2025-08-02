from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

s1 = "Harsh is an intelligent boy"
s1s = sia.polarity_scores(s1)
print(s1)
print(s1s)

#uppercase
s2 = "Harsh is an INTELLIGENT boy"
s2s = sia.polarity_scores(s2)
print(s2)
print(s2s)

#degree modifier
s3 = "Harsh is an very intelligent boy"
s3s = sia.polarity_scores(s3)
print(s3)
print(s3s)

#punctuation
s4 = "Harsh is an intelligent boy !!!"
s4s = sia.polarity_scores(s4)
print(s4)
print(s4s)

#emoticons
s5 = "Harsh is an intelligent boy :)"
s5s = sia.polarity_scores(s5)
print(s5)
print(s5s)

#neutral
s6 = "Harsh is a naughty boy"
s6s = sia.polarity_scores(s6)
print(s6)
print(s6s)

#negative
s7 = "Harsh is a bad boy"
s7s = sia.polarity_scores(s7)
print(s7)
print(s7s)

#conjunction
s8 = "Harsh is an INTELLIGENT boy but at times he is bad"
s8s = sia.polarity_scores(s8)
print(s8)
print(s8s)

#slangs
s9 = "This hotel sucks"
s9s = sia.polarity_scores(s9)
print(s9)
print(s9s)

