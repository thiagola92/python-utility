from deep_get import dget

def get_from_dict(dictionary, keys_and_paths, fail=None):
  output = {}

  for key, path in keys_and_paths:
    output[key] = dget(dictionary, path, fail)

  return output