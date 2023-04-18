import numpy as np
import math
import os
import matplotlib.pyplot as plt

class BikeModel:
    def __init__(self, x=0, y=0, theta=math.radians(90)):
        self.x = x
        self.y = y
        self.theta = theta

    def bicycle(self, speed, steer, d_time):
        beta = np.arctan(0.5 * np.tan(steer))
        dx = speed * np.cos(beta + self.theta) * d_time
        dy = speed * np.sin(beta + self.theta) * d_time
        d_theta = (speed * np.tan(steer) * np.cos(beta))/3

        self.x += dx
        self.y += dy
        self.theta += d_theta

        return self.x, self.y, self.theta
