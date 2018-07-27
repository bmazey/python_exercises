class MovieQueue:
    """MovieQueue class."""
    def __init__(self):
        self.queue = list()

    def populate_movie_queue(self):
        """populates a new MovieQueue"""

        self.queue.append('Donatello')
        self.queue.append('Raphael')
        self.queue.append('Michelangelo')
        self.queue.append('Leonardo')
