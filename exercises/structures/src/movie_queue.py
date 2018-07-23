class MovieQueue:
    """MovieQueue class."""
    def __init__(self):
        self.queue = list()

    def populate_movie_queue(self):
        """populates a new MovieQueue"""
        # TODO - implement this method!
        # list of people
        peeps =["Donatello","Raphael","Michelangelo","Leonardo"]
        # adds people to queue
        for name in peeps:
            self.queue.append(name)

