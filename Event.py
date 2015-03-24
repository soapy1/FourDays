class Event(object):

    def __init__(self, ov, oo, d, ne, c):
        # the option number (from above)
        self.opt_value = ov
        # the outcome of choose this option
        self.opt_outcome = oo
        # a description of the current conditions
        self.description = d
        # a  list of next events
        self.next_event = ne
        # a desctipyion of the challenge for the user (if applicable) form:
        # challenge = {'word':'sorry', 'time':10}
        self.challenge = c
