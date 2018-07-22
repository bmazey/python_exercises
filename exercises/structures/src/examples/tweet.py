# for simplicity mock up some tweets
from exercises.structures.src.examples.handle import Handle
from exercises.structures.src.examples.twitter_user import TwitterUser
from exercises.structures.src.examples.enhanced_twitter_user import EnhancedTwitterUser
from collections import namedtuple
import random


# borrowed from https://pybit.es/python-data-model.html
def generate_tweets():
    Tweet = namedtuple('Tweet', 'time text likes')

    tweets = (
        Tweet('2017-01-25 08:45:00', 'Teaching Python today, feels great', 3),
        Tweet('2017-01-25 09:45:00', 'Writing a post on the Python data model', 2),
        Tweet('2017-01-25 07:45:00', 'from __future__ import braces ... not a chance', 10),
        Tweet('2017-01-25 10:45:00', 'Doing code challenge 03, learning a lot', 5),
        Tweet('2017-01-25 12:45:00', 'Done with code challenge 03', 1),
    )
    print(tweets)
    return tweets


def generate_more_tweets():
    Tweet = namedtuple('Tweet', 'time text likes')

    tweets = (
        Tweet('2017-01-25 10:46:00', 'Writing a blog post on a cool new module I discovered', 5),
        Tweet('2017-01-25 12:46:00', 'Learning some Python today, feeling great', 15),
    )
    print(tweets)
    return tweets


def main():
    bob = TwitterUser(Handle('bbelderbos', shared_handle='pybites'), generate_tweets())

    # implementing len we can call it on the object like this:
    # print(len(bob))

    # implementing getitem we can get tweets by index
    # print(bob[0])

    # or with a slice
    # print(bob[-2:])

    # wow implementing __getitem__ bob turns into an iterable!
    # for tweet in bob:
        # print(tweet)

    # and can be passed as a sequence object to other builtins
    # random.choice(bob)

    # or give it to sorted so we can use its key arg to sort by most likes
    # easter eggs are well received :)
    # for tw in sorted(bob, key=lambda x: x.likes, reverse=True):
        # print(tw)

    julian = TwitterUser(Handle('techmoneykids', shared_handle='pybites'), generate_more_tweets())

    # I want to be able to merge tweets, just as we can do with lists: [1] + [2,3] = [1,2,3]
    # however this does not work out of the box
    # print(bob + julian)

    # let's re-instantiate as a new class which supports merging tweets
    bob = EnhancedTwitterUser(Handle('bbelderbos', shared_handle='pybites'), generate_tweets())
    julian = EnhancedTwitterUser(Handle('techmoneykids', shared_handle='pybites'), generate_more_tweets())

    # lets also add a not-compatible handle
    stranger = EnhancedTwitterUser(Handle('someblogger', shared_handle='stranger'), generate_more_tweets())

    # now it works, thanks to __add__
    # pybites = bob + julian
    # print(pybites)

    # our tweets are merged, glad to have Julian most liked tweet now ;)
    # for tw in sorted(pybites, key=lambda x: x.likes, reverse=True):
        # print(tw)

    # but stranger is not part of pybites, so custom exception is raised (as implemented in __add__)
    # bob + stranger

    # print on object calls the underlying __str__ which we used to print some stats
    # also notes it embeds the __str__ of the Handle object
    # print(bob)

    # Julian is definitely more influential than me :)
    # print(julian)

    # ... improving the average
    # print(pybites)


if __name__ == 'main':
    main()