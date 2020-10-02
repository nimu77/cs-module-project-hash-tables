def no_dups(s):

    words = s.split()

    # store words
    d = {}

    a = []

    for word in words:
        if word not in d:
            d[word] = True
            a.append(word)
        else:
            continue
    return ' '.join(a)


    # Your code here
    # d = set(s.split())
    # print(d)
    # d = set()

    # for word in s.split():
    #     if word in d:
    #         pass
    #     else:
    #         d += f"{word} "
    # # print(type(d))
    # return d
    # t = ''
    # for word in d:
    #     if word in t:
    #         pass
    #     else:
    #         t += word + ' '
    # return t

    # d = {}

    # words = s.split()

    # for word in words:
    #     if word not in d:
    #         d[word] = word
    # for i in range(len(d)):
    #     for k, v in d.items():
    #         return v

    # words = set(s.split())
    # words = ' '.join(words)
    # words = []

    # for word in s.split():
    #     if word in words:
    #         pass
    #     else:
    #         words += word
            


    #     return words
# print(no_dups('hello hello cats dogs'))

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))