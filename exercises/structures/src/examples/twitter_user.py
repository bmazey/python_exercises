# a TwitterUser has a handle name and a bunch of tweets, note the two dunder methods after the constructor ...


class TwitterUser(object):
    # borrowed from https://pybit.es/python-data-model.html
    def __init__(self, handle, tweets):
        self.handle = handle
        self._tweets = tweets

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, position):
        return self._tweets[position]
