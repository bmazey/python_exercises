# we can make this work implementing __add__()


class IncompatibleHandle(Exception):
    pass


class EnhancedTwitterUser(object):

    def __init__(self, handle, tweets):
        self.handle = handle
        self.tweets = tweets  # making interface public as we need it in __add__

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, position):
        return self.tweets[position]

    def __add__(self, other):
        if self.handle.shared_handle != other.handle.shared_handle:
            raise IncompatibleHandle('Not the same shared handle, cannot merge tweets')
        all_tweets = self.tweets + other.tweets
        return EnhancedTwitterUser(self.handle.shared_handle, all_tweets)

    # adding object string representation methods
    def __repr__(self):
        return 'TwitterUser(%r, %r)' % (self.handle, self.tweets)

    # difference between the repr and str:
    # http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
    def __str__(self):
        return '{} => likes: {} for {} tweets = {:.1f} avg'.format(
            self.handle, self.total_likes(),
            len(self), self.avg_likes()
        )

    # adding some public methods to show later on that the merged object behaves just as its parts
    def total_likes(self):
        return sum(tw.likes for tw in self.tweets)

    def avg_likes(self):
        return self.total_likes() / len(self)
