'''
6 kyu
Name: Projectile Motion
https://www.codewars.com/kata/5af96cea3e9715ec670001dd
'''

import math


class Projectile:
    def __init__(self, height: float, velocity: float, angle: float):
        self._height = float(height)
        self.velocity = float(velocity)
        self.angle = angle

    def height_eq(self):
        if self._height != 0:
            return "h(t) = -16.0t^2 + " + str(
                round((self.velocity * math.sin(math.radians(self.angle))), 3)) + "t + " + str(self._height)
        else:
            return "h(t) = -16.0t^2 + " + str(round((self.velocity * math.sin(math.radians(self.angle))), 3)) + "t"

    def horiz_eq(self):
        return "x(t) = " + str(round((self.velocity * math.cos(math.radians(self.angle))), 3)) + "t"

    def height(self, t):

        return round(- 16 * t ** 2 + self.velocity * math.sin(math.radians(self.angle)) * t + self._height, 3)

    def horiz(self, t):

        return round(self.velocity * math.cos(math.radians(self.angle)) * t, 3)

    def landing(self):

        discr = (self.velocity * math.sin(math.radians(self.angle))) ** 2 + 4.0 * 16.0 * (self._height)
        if discr > 0:
            t1 = (-self.velocity * math.sin(math.radians(self.angle)) + math.sqrt(discr)) / (-32)
            t2 = (-self.velocity * math.sin(math.radians(self.angle)) - math.sqrt(discr)) / (-32)

            t = max(t1, t2)

        elif discr == 0:
            t = (-self.velocity * math.sin(math.radians(self.angle))) / (-32)

        x = self.velocity * math.cos(math.radians(self.angle)) * t

        return [round(x, 3), 0, round(t, 3)]