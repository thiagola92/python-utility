def dget(structure, key_list, error=None):
  for key in key_list:
    try:
      structure = structure[key]
    except:
      return error

  return structure