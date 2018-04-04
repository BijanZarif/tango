import numpy as np
import math as m


class PipeStructure:
    def __init__(self, parameters):
        l = parameters['l']  # Length
        self.d = parameters['d']  # Diameter
        self.rhof = parameters['rhof']  # Density

        e = parameters['e']  # Young's modulus of structure
        h = parameters['h']  # Thickness of structure
        self.cmk2 = (e * h) / (self.rhof * self.d)  # Wave speed squared of outlet boundary condition

        self.m = parameters['m']  # Number of segments
        self.dz = l / self.m  # Segment length
        self.z = np.arange(self.dz / 2.0, l, self.dz)  # Data is stored in cell centers

        self.n = 0  # Time step
        self.dt = 0  # Time step size

        # Initialization
        self.p = np.ones(self.m) * 2.0 * self.cmk2  # Pressure
        self.a = np.ones(self.m) * m.pi * self.d ** 2 / 4.0  # Area of cross section
        self.p0 = 2.0 * self.cmk2  # Reference pressure
        self.a0 = m.pi * self.d ** 2 / 4.0  # Reference area of cross section

        self.initialized = False
        self.initializedstep = False

    def getinputgrid(self):
        return self.z

    def setinputgrid(self, z):
        if np.linalg.norm(self.z - z) / np.linalg.norm(self.z) > np.finfo(float).eps:
            Exception('Mapper not implemented')

    def getoutputgrid(self):
        return self.z

    def setoutputgrid(self, z):
        if np.linalg.norm(self.z - z) / np.linalg.norm(self.z) > np.finfo(float).eps:
            Exception('Mapper not implemented')

    def gettimestep(self):
        return self.dt

    def settimestep(self, dt):
        if self.initializedstep:
            Exception('Step ongoing')
        else:
            self.dt = dt

    def initialize(self):
        if self.initialized:
            Exception('Already initialized')
        else:
            self.initialized = True

    def initializestep(self):
        if self.initialized:
            if self.initializedstep:
                Exception('Step ongoing')
            else:
                self.n += 1
                self.initializedstep = True
        else:
            Exception('Not initialized')

    def calculate(self, p):
        # Independent rings model
        self.p = p
        for i in range(len(self.a)):
            self.a[i] = self.a0 * ((self.p0 - 2.0 * self.cmk2) / (self.p[i] - 2.0 * self.cmk2)) ** 2
        # Return copy of output
        return np.array(self.a)

    def finalizestep(self):
        if self.initialized:
            if self.initializedstep:
                self.initializedstep = False
            else:
                Exception('No step ongoing')
        else:
            Exception('Not initialized')

    def finalize(self):
        if self.initialized:
            self.initialized = False
        else:
            Exception('Not initialized')
