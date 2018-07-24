# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pat, txt, q):
    # TODO - implement this method!
    pat_len = len(pat)
    txt_len = len(txt)
    i = 0
    j = 0
    pat_hash = 0  # hash value for pattern
    txt_hash = 0  # hash value for txt
    h = 1
    matches = list()

    # The value of h would be "pow(d, pat_len-1)%q"
    for i in range(pat_len - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(pat_len):
        pat_hash = (d * pat_hash + ord(pat[i])) % q
        txt_hash = (d * txt_hash + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(txt_len - pat_len + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if pat_hash == txt_hash:
            # Check for characters one by one
            for j in range(pat_len):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            # if pat_hash== txt_hashand pat[0...pat_len-1] = txt[i, i+1, ...i+pat_len-1]
            if j == pat_len:
                matches.append(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < txt_len - pat_len:
            txt_hash= (d * (txt_hash- ord(txt[i]) * h) + ord(txt[i + pat_len])) % q

            # We might get negative values of t, converting it to
            # positive
            if txt_hash< 0:
                txt_hash = txt_hash + q

    return matches
