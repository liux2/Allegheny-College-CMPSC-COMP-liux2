import spacy
from spacy_langdetect import LanguageDetector

nlp = spacy.load("en")
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
text = "This is an english text."
doc = nlp(text)
# document level language detection. Think of it like average language of the document!
# print(type(doc._.language))
if doc._.language["language"] == "en":
    print(doc._.language["language"])
# sentence level language detection
# for sent in doc.sents:
#     print(sent, sent._.language)
a = "n"
if a is not None and doc._.language["language"] == "en":
    print("True")
