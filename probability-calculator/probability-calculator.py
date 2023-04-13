import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, amount):
        if amount > len(self.contents):
            return self.contents
        else:
            drawn = random.sample(self.contents, k=amount)
            for ball in drawn:
                self.contents.remove(ball)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat1 = copy.deepcopy(hat)
        drawn_balls = hat1.draw(num_balls_drawn)
        are_in = True
        for color, value in expected_balls.items():
            for x in range(value):
                if color in drawn_balls:
                    drawn_balls.remove(color)
                else:
                    are_in = False
                    break
            if not are_in:
                break
        if are_in:
            count = count + 1
    probability = count / num_experiments
    return probability
