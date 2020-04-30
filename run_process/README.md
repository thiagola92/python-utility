# run-process
Creates a process to run an function and gives you a queue to receive values from function.  
The function first argument **must** be the queue.  

# usage
```python
def add(queue, n1, n2):
  queue.put(n1 + n2)

queue = run_process(add, 1, 2)
result = queue.get()

print(result) # 3
```