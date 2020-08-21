sentence = "bir berber, bireberber gel beraber 1'inde iş yapalım"

dictionary = {}

for i in sentence:
    keys = dictionary.keys()
    if i in keys:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
dictionary
