class Singleton:
    _instance = None  # This is where the one-and-only instance lives

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the singleton instance... because one is enough. 😎")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):  # Prevents reinitialization
            self.value = value
            self.initialized = True

# Testing it out:
s1 = Singleton("First Instance")
s2 = Singleton("Second Instance")

print(s1.value)  # Output: First Instance
print(s2.value)  # Output: First Instance