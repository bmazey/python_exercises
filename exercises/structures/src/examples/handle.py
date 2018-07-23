# lets make twitter handle a bit more sophisticated, we are going to work with a parent-child relation for this example


class Handle(object):
    # borrowed from https://pybit.es/python-data-model.html
    def __init__(self, handle, shared_handle=None):
        self.handle = handle
        self.shared_handle = shared_handle

    def __str__(self):
        if self.shared_handle is None:
            shared = ''
        else:
            shared = ' (shared handle: {})'.format(self.shared_handle)
        return '{}{}'.format(self.handle, shared)
