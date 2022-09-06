import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key,value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, amount):
        balls_del =[]
        if amount >= self.countents:
            return self.contents
        for i in range(amount):
            wich =self.countents.pop(int(random.randrange(0, len(self.contents))))
            balls_del.append(wich)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count=0
    for _ in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      temp_list = copyhat.draw(num_balls_drawn)
      success=True
      for key,value in expected_balls.items():
        if temp_list.count(key) < value:
          success=False
          break
      if success:
        final_count+=1
    return final_count/num_experiments
