def rename_key(dictionary, key, new_key):
  dictionary[new_key] = dictionary[key]
  del dictionary[key]