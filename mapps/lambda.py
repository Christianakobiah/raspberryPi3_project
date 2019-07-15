from functools import reduce
def join_string(words):
    tee = ""
    for word in words:
        tee += word + " "
    return tee
words = ['C','h','r','i','s','t','i','a','n','a']
total = reduce(lambda item, running_total: item + " " + running_total , words)
print(total)
    
Christiana = join_string(words)
print(join_string(words))