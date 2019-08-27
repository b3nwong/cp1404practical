user_input= input("Please type in your text: ")

text_list = user_input.split()

text_list.sort()

word_occurrences={}

for word in text_list:
    if word not in word_occurrences:
        word_occurrences[word]=1
    else:
        word_occurrences[word]+=1

for x,y in word_occurrences.items():
    print("{}:{}".format(x,y))
