import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs.keys():
            for i in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, balls_to_draw):
        if balls_to_draw >= len(self.contents):
            balls_drawn = copy.deepcopy(self.contents)
            random.shuffle(balls_drawn)
            self.contents.clear()
            random.shuffle(balls_drawn)
            return balls_drawn
        else:
            balls_drawn = random.sample(self.contents, balls_to_draw)
            for item in balls_drawn:
                self.contents.remove(item)
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for i in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat)
        current_draw = one_experiment(copy_of_hat, expected_balls, num_balls_drawn)
        if current_draw:
            num_success += 1
    return num_success / num_experiments


def one_experiment(hat, expected_balls, num_balls_drawn):
    success = True
    current_draw_dict = {}
    current_draw = hat.draw(num_balls_drawn)
    for index in range(len(current_draw)):
        current_draw_dict[current_draw[index]] = current_draw.count(current_draw[index])
    for key in expected_balls.keys():
        if key in current_draw_dict.keys():
            if current_draw_dict[key] < expected_balls[key]:
                success = False
                break
        else:
            success = False
            break
    return success


