from Algorithm import *


def checker(text):
    arr = pd.Series(text)
    arr.apply(process)
    arr = vectorize_train(arr)
    x = mnb.predict(arr)[0]
    return x