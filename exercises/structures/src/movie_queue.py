class MovieQueue:
    """MovieQueue class."""
    def __init__(self):
        self.queue = list()

    def populate_movie_queue(self):
        """populates a new MovieQueue"""
        # TODO - implement this method!
        people = ["Donatello", "Raphael", "Michelangelo", "Leonardo"]

        for name in people:
            self.queue.append(name)

