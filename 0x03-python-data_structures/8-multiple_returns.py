#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        c1 = sentence[0]
    else:
        c1 = None

    return (len(sentence), c1)
