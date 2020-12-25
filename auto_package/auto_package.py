import gc

class AutoPackage():
    """
    A package to store a list of items until it fills up.
    When full, send all items to your destination.
    """

    def __init__(self, send_function, size=1000000):
        self.send_function = send_function
        self.size = int(size)

        self.package = []
    
    def add(self, item, *args, **kwargs):
        self.package.append(item)

        if len(self.package) >= self.size:
            self.send(*args, **kwargs)

    def send(self, *args, **kwargs):
        if len(self.package) > 0:
            self.send_function(self.package, *args, **kwargs)
        
        self.package.clear()

        gc.collect()