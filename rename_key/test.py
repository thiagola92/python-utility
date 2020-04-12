from rename_key import rename_key

def main():
  first = {
    'nome': 'thiago',
    'idade': 27
  }

  print(first)
  rename_key(first, 'nome', 'name')
  print(first)

main()