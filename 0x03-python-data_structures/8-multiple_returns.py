#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        first = sentence[0]
    else:
        None

    return (len(sentence), first)
