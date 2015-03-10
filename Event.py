class Event:
    def __init__(on, ov, oo, d, ne, c):
        # the option selection (from above)
        self.opt_number = on
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
        
        
