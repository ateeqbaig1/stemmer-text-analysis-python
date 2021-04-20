# Online Python compiler (interpreter) to run Python online.
def pos(sentense):
    """
    finds the root word for each word in the input sentense, and output in the form of a sentense.
    """

    words = list(sentense.split(sep=" "))
    vowels = "aeiouy"

    stemmed = []
    for word in words:
        if word.endswith(("'s", "s'")):
            word = word.replace("'s", "")
            word = word.replace("s'", "")
        if word.endswith("s") and word[-2] not in vowels:
            word = word.replace("s", "")
        if word.endswith("sses"):
            word = word.replace("sses", "ss")
        if word.endswith("ies"):
            if len(word[:-2]) <= 2:
                word = word.replace("s", "")
            elif len(word[:-2]) > 2:
                word = word.repalce("ies", "i")
        if word.endswith("ed") and not (word.endswith("ied")):
            word = word.replace("ed", "")
        if word.endswith("ied"):
            if len(word[:-2]) <= 2:
                word = word.replace("d", "")
            elif len(word[:-2]) > 2:
                word = word.replace("ied", "i")
        if word.endswith(("lying", "ingly", "erly", "ly", "er")):
            word = word.replace("lying", "")
            word = word.replace("ingly", "")
            word = word.replace("erly", "")
            word = word.replace("ly", "")
            word = word.replace("er", "")
        if word.endswith("ing") and len(word[:-3]) >= 3:
            word = word.replace("ing", "", 1)

        stemmed.append(word)

    return " ".join(stemmed)


stemmed1 = pos(
    "The consensus chopped off last Friday while the voters were tied down flying without counting properly so wasn't a great day after all"
)
stemmed2 = pos(
    "I went to BTS concert with my bonus pay and I cried there as my heart melted away from their singing, it was utterly beautiful I just felt possessed"
)
stemmed3 = pos(
    "it's name was theirs' to say and with gaps they smelled gas and this was not okay."
)
stemmed4 = pos(
    "today is a lovely day while my CMPS was not the best and it's days are over but oh well what could be done about it right?"
)

stemmed5 = pos("f")
print(stemmed1)
print(stemmed2)
print(stemmed3)
print(stemmed4)
print(stemmed5)
