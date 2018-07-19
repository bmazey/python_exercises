from random import sample


class PasswordGenerator(object):
    @staticmethod
    def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

        a = sample(letters, 1)
        b = sample(letters, 1)
        c = sample(letters, 1)
        d = sample(letters, 1)
        e = sample(letters, 1)

        f = sample(numbers, 1)
        g = sample(numbers, 1)
        h = sample(numbers, 1)
        i = sample(numbers, 1)

        j = sample(symbols, 1)

        password = (str(a[0]) + str(b[0]) + str(c[0]) + str(d[0]) + str(e[0]) + str(f[0]) + str(g[0]) + str(h[0]) +
                    str(i[0]) + str(j[0]))
        return password
