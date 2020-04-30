from run_process import run_process

def example1(queue, param1, param2):
  print(param1)
  print(param2)

  queue.put('end example 1')

queue = run_process(example1, 10, 15)
result = queue.get()
print(result)


def example2(queue, param1, param2):
  print(param1)
  print(param2)

  queue.put('end example 2')

queue = run_process(example2, param1=20, param2=30)
result = queue.get()
print(result)


def example3(queue, param1, param2):
  print(param1)
  print(param2)

  queue.put('end example3')

queue = run_process(example3, 40, param2=50)
result = queue.get()
print(result)