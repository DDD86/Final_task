class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def get_count(self):
        return self.count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            raise Exception("Counter was not used in a proper try-with-resources block")
