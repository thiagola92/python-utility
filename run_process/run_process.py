import multiprocessing

def run_process(function, *args, **kwargs):
  queue = multiprocessing.Queue()

  process = multiprocessing.Process(
    target=function,
    args=(queue, *args),
    kwargs=kwargs,
    daemon=True
  )

  process.start()
  
  return queue
