import random
import copy

class Hat:
	def __init__(self, **kwargs):
		self.balls = ""
		for color, balls in kwargs.items():
			self.balls += (color + " ") * balls
		self.contents = self.balls.split()
	
	def draw(self, draws):
		if draws > len(self.contents):
			return self.contents
		else:
			self.drawn_balls = random.sample(self.contents, k=draws)
			for ball in range(len(self.drawn_balls)):
				self.contents.remove(self.drawn_balls[ball])
			return self.drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	success_cases = 0
	for n_exp in range(num_experiments):
		exp_hat = copy.deepcopy(hat)
		exp_draws = exp_hat.draw(num_balls_drawn)
		
		count_balls = list()
		count_expected = list()
		for color in expected_balls:
			count_expected.append(expected_balls[color])
			count_balls.append(exp_draws.count(color))
			
		if count_balls >= count_expected:
			success_cases += 1
				
	probability = success_cases/num_experiments
	return probability