from multiprocessing import Process

BASE = 11
NUM_PS = BASE
ERROR_THRESHOLD = 0.2
LENGTH = 7
MAX = BASE**LENGTH


candiates_sum = {
  0: "a", 
  1: "b",
  2: "c",
  3: "d",
  4: "e",
  5: "f",
  6: "g",
  7: "h", 
  8: "j",
  9: "k",
  10: "l"
}

training_set = {
  "1122936": "d",
  "1122965": "a",
  "1122983": "c",
  "1122763": "c",
  "1122887": "l",
  "1110284": "j",
  "1110658": "l",
  "1220787": "k",
  "1021352": "a",
  "1020216": "c",
  "1010118": "b",
}


def calculate_check_sum(lst, weight):
  sum = 0
  assert len(lst)==len(weight)
  for i in xrange(len(lst)):
    sum += lst[i]*weight[i]
  return sum



class Worker(Process):
  def __init__(self, lower, upper):
    super(Worker, self).__init__()
    self.lower = lower
    self.upper = upper
  def run(self):
    for offset in range(1): # offset does not matter now
      for i in xrange(self.lower, self.upper): 

        weight = []
        for j in xrange(LENGTH):
          weight.append(i%(BASE))
          i /= BASE
        weight.reverse()

        error = 0
        # print "checking %s"%(str(weight))
        for key, item in training_set.items():
          temp = map(lambda x: int(x), " ".join(key).split(" "))
          check_sum = calculate_check_sum(temp, weight)
          
          if not candiates_sum[(check_sum+offset)%11]==item:
            error+=1

        error_rate = float(error)/len(training_set)
        if error_rate>=ERROR_THRESHOLD:
          continue
        else: 
          result = "offset: %d, %s, error_rate: %f"%(offset, str(weight), error_rate)
          print result
         


if __name__ == "__main__":
  workers = {}
  for i in xrange(NUM_PS):
    workers[i] = Worker(i*MAX/NUM_PS, (i+1)*MAX/NUM_PS)
    workers[i].start()

  for i in xrange(NUM_PS):
    workers[i].join()
