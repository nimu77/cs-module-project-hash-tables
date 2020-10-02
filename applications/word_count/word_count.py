def word_count(s):
    # Your code here
    d = {}

    
    bad_chars = '":;,.-+=/\\|[]{}()*^&\`\"\t\r\n\f\b'

    for c in bad_chars:
        s = s.replace(c, '')

    print(s)
    for i in s.lower().split():

        if i not in d:
            d[i] = 1

        else:
            d[i] +=1

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))