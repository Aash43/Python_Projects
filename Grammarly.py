from textblob import TextBlob
Blob = TextBlob("Apple does not hav reasonably priced phones")

a = Blob.correct()


print(a)


Randomt = TextBlob("Comment vas-tu?")

print(Randomt.detect_language())

print(Randomt.translate(to='es'))
print(Randomt.translate(to='en'))
print(Randomt.translate(to='zn'))