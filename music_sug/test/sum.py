import pytextrank
import spacy
import py_stringmatching as sm

user_text = """
I am strong, I believe I can protect my children.
My boy doesn't have his father. I am the only one he has.
I saw you cry a lot, please don't be. I promise I will give you a good life.
"""
# user_text = "You are the love of my life, my son. My son doesn't have his father."

lyrics = """Call it love and devotion
Call it a mom's adoration
Foundation
A special bond of creation,
Ha

For all the single moms out there
Going through frustration
Clean Bandit, Sean-da-Paul, Anne-Marie
Sing, make them hear

She works the nights by the water
She's gone astray so far away
From my father's daughter
She just wants a life for her baby
All on her own, no one will come
She's got to save him

Daily struggle

She tells him, "Ooh, love, no one's ever gonna hurt you, love.
I'm gonna give you all of my love.
Nobody matters like you."

Stay out there, stay out there

She tells him, "Your life ain't gon' be nothing like my life.
You're gonna grow and have a good life.
I'm gonna do what I've got to do."

Stay out there, stay out there

So, rockabye baby, rockabye
I'm gonna rock you
Rockabye baby, don't you cry
Somebody's got you
Rockabye baby, rockabye
I'm gonna rock you
Rockabye baby, don't you cry
Rockabye, no

Rockabye-rocka-rocka-rocka-bye
Rockabye, yeah, oh, oh
Rockabye-rocka-rocka-rocka-bye

Single mama, you doing out there
Facing the hard life without no fear, yeah
Just so you know that you really care
'Cause any obstacle come you're well prepared,
Oh, no
No, mama, you never shed tear
'Cause you have to shed things year after year
And you give the youth love beyond compare, yeah
You find his school fee and the bus fare, yeah

Mmm, Marie, the pops' disappear
In the round back can't find him nowhere
Steadily you work flow, everything you know
Say you nah stop no time – no time for your jear

Now she got a six-year-old
Trying to keep him warm
Trying to keep out the cold
When he looks in her eyes
He don't know he is safe

When she says, "Ooh, love, no one's ever gonna hurt you, love.
I'm gonna give you all of my love.
Nobody matters like you."

So, rockabye baby, rockabye
I'm gonna rock you
Rockabye baby, don't you cry
Somebody's got you
Rockabye baby, rockabye
I'm gonna rock you
Rockabye baby, don't you cry

Oh-badda-bang-bang-bang, alright then

Rockabye, no

Rockabye-rocka-rocka-rocka-bye
Rockabye, yeah, oh, oh
Rockabye-rocka-rocka-rocka-bye

Rockabye, don't bother cry
Lift up your head, lift it up to the sky
Rockabye, don't bother cry
Angels surround you, just dry your eye

Now she got a six-year-old
Trying to keep him warm
Trying to keep out the cold
When he looks in her eyes
He don't know he is safe when she says...

She tells him, "Ooh, love, no one's ever gonna hurt you, love.
I'm gonna give you all of my love.
Nobody matters like you."

Stay out there, stay out there

She tells him, "Your life ain't gonna be nothing like my life. Stay.
You're gonna grow and have a good life.
I'm gonna do what I've got to do."

So, rockabye baby, rockabye
Rockabye-rocka-rocka-rocka-bye
I'm gonna rock you
Rockabye baby, don't you cry
Rockabye-rocka-rocka-rocka-bye
Somebody's got you
Rockabye baby, rockabye
Rockabye-rocka-rocka-rocka-bye
I'm gonna rock you
Rockabye baby, don't you cry
Oh-badda-bang-bang-bang, alright then
Rockabye

Rockabye, don't bother cry
Lift up your head, lift it up to the sky. Rockabye
Rockabye, don't bother cry, yeah
Angels surround you, just dry your eye, yeah

Rockabye, don't bother cry, no
Lift up your head, lift it up to the sky, oh
Rockabye, don't bother cry
Angels surround you, just dry your eye"""

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logger = logging.getLogger("PyTR")

# doc = nlp(lyrics)

# print("pipeline", nlp.pipe_names)
# print("elapsed time: {} ms".format(tr.elapsed_time))
# for phrase in doc._.phrases:
#     print("{:.4f} {:5d}  {}".format(phrase.rank, phrase.count, phrase.text))
#     print(phrase.chunks)
# for phrase in doc._.phrases[:20]:
#     print(phrase)


def word_bag_list(org_text):
    # ws_tok_set = sm.WhitespaceTokenizer(return_set=True)
    qg3_tok_set = sm.QgramTokenizer(qval=3, return_set=True)
    nlp = spacy.load("en_core_web_sm")

    tr = pytextrank.TextRank(logger=None)
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(org_text)

    whole_sent = ""
    for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
        # pattern = re.compile(r"[\W_]+")
        # print(pattern.sub(" ", repr(sent)).lower())
        whole_sent = whole_sent + repr(sent).rstrip() + " "
    # print(ws_tok_set.tokenize(whole_sent))
    # return qg3_tok_set.tokenize(whole_sent)
    return [whole_sent]


def compare(user_sum, lyrics_sum):
    me = sm.MongeElkan()
    return me.get_raw_score(user_sum, lyrics_sum)


print(compare(word_bag_list(user_text), word_bag_list(lyrics)))
