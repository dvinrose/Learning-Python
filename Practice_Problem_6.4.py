'''

Implement function wordcount() that takes as input a text—as a string— and prints the
frequency of each word in the text. You may assume that the text has no punctuation and
words are separated by blank spaces.
text = 'all animals are equal but some \
animals are more equal than others'

wordCount(text)

all appears 1 time.
animals appears 2 times.
some appears 1 time.
equal appears 2 times.
but appears 1 time.
are appears 2 times.
others appears 1 time.
than appears 1 time.
more appears 1 time.

'''

text = 'all animals are equal but some animals are more equal than others'
list = text.split()

def wordcount(itemList):

    counters = {}

    for item in itemList:
        if item in counters:
         counters[item] += 1
        else:
         counters[item] = 1
    return counters

x = wordcount(list)

def main():

    for i in x:
     if x[i] > 1:
        print(i, "appears", x[i], "times")
     else:
        print(i, "appears", x[i], "time")

main()