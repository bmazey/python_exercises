# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number

# hash value for pattern
# hash value for txt
def search(pat, txt, q):
    m = len(pat)
    n = len(txt)
    j = 0
    p = 0
    t = 0
    h = 1
    matches = list()

    for i in range(m-1):
        h = (h*d) % q
    # calculate the has value of pattern and first window of text
    for i in range(m):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q
    # slide the pattern over text one by one
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if txt[i+j] != pat[j]:
                    break
            j += 1
            if j == m:
                matches.append(i)

        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q
            if t < 0:
                t = t+q

    return matches
