from rename_key import rename

def main():
  first = {
    'nome': 'thiago',
    'idade': 27
  }

  print(first)
  rename(first, 'nome', 'name')
  print(first)

main()