import pytextrank
import spacy
import py_stringmatching as sm


def word_bag_list(org_text):
    """Take text and do sum, return sumed sentence list."""
    # load language model
    nlp = spacy.load("en_core_web_sm")
    # init pytextrank, then add pipe
    tr = pytextrank.TextRank(logger=None)
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
    # declear text
    doc = nlp(org_text)
    # merge results into one string
    whole_sent = ""
    for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
        whole_sent = whole_sent + repr(sent).rstrip() + " "
    return [whole_sent]


def compare_sum(user_sum, lyrics_sum):
    """Take two sentence list and compare, return closeness score."""
    # init monge elkan algo
    me = sm.MongeElkan()
    return me.get_raw_score(user_sum, lyrics_sum)
