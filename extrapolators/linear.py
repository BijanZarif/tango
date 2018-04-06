import numpy as np


class Linear:
    def __init__(self, *_):
        self.n = 0
        self.xp = np.array([])
        self.x = np.array([])
        self.xn = np.array([])
        self.added = False

    def initialize(self, x):
        self.xp = np.array(x)
        self.x = np.array(x)
        self.xn = np.zeros_like(x)

    def add(self, x):
        self.xp = np.array(x)
        self.added = True

    def predict(self):
        self.xp = 2.0 * self.x - self.xn
        return np.array(self.xp)

    def initializestep(self):
        self.n += 1
        self.xn = self.x
        self.x = self.xp

    def finalizestep(self):
        if self.added:
            self.added = False
        else:
            raise RuntimeError("No information added during step")
