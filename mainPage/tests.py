def getQueryBuy(queryDict):
    # {'csrfmiddlewaretoken': ['gQJKvsznZiBU8q3ju3TeuQaRf7QpqPW1idLYswdKXtAgyHWsq6iwjkEaIBI0mSTp'], 'kantarNo': [''],
    #  'tarih': [''], 'tedarikci': ['1'], 'malTipi': ['']}
    queryDict2={}
    for field in queryDict.keys():
        if queryDict[field] == ['']:
            pass
        else:
            queryDict2[field]=queryDict[field]
    return queryDict2
print(getQueryBuy(
{'csrfmiddlewaretoken': ['gQJKvsznZiBU8q3ju3TeuQaRf7QpqPW1idLYswdKXtAgyHWsq6iwjkEaIBI0mSTp'], 'kantarNo': [''],
 'tarih': [''], 'tedarikci': ['1'], 'malTipi': ['']}
))
