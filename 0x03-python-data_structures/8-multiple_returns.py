#!/usr/bin/python3

def multiple_returns(sentence):
    tup = len(sentence) if sentence else 0, sentence[0] if len(sentence) \
            else None
    return tup
