import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  a = np.array(list)
  a = np.reshape(a, (3, 3))

  sum = [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum()]
  mean = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()]
  variance = [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var()]
  std = [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std()]
  max = [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max()]
  min = [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min()]

  calculations = {'mean': mean, 'variance': variance, 'standard deviation': std, 'max': max, 'min': min, 'sum': sum}

  return calculations