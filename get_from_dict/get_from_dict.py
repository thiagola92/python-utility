from deep_get import dget

def get_from_dict(dictionary, keys_and_paths):
  output = {}

  for key, path in keys_and_paths:
    output[key] = dget(dictionary, path, None)

  return output