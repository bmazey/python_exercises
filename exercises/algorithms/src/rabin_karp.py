# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pat, txt, q):
    # TODO - implement this method!
    n = len(txt)
    m = len(pat)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):  # preprocessing
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for s in range(n - m + 1):  # note the +1
        if p == t:  # check character by character
            match = True
            for i in range(m):
                if pat[i] != txt[s + i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n - m:
            t = (t - h * ord(txt[s])) % q  # remove letter s
            t = (t * d + ord(txt[s + m])) % q  # add letter s+m
            t = (t + q) % q  # make sure that t >= 0
    return result
    # matches = list()
    # return matches
