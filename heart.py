class Heart:
    def __init__(self):
        self.bpm =72

    def beat(self):
        print("Lub-dub")

    def __str__(self):
        return f"Heart is beating at {self.bpm}"
