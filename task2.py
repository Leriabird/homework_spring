class fibonacci_sequence:
    def __init__(self, len_seq):
        self.len_seq = len_seq
        self.counter = 0
        self.initial = 1
        self.increment = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.len_seq:
            self.counter += 1
            new_seq_elt = self.initial + self.increment
            self.initial = self.increment
            self.increment = new_seq_elt
            return new_seq_elt
        else:
            raise StopIteration
