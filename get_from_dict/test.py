from get_from_dict import get_from_dict

dictionary = {
  'age': 27,
  'name': 'thiago',
  'grades': [
    10,
    20,
    30
  ],
  'family': {
    'mom': 'mother\'s name',
    'father': 'father\'s name'
  },
  'class': {
    'professor': 'marcelo',
    'schedule': [
      {
        'hour': '17:50',
        'duration': 1
      },
      {
        'hour': '13:50',
        'duration': 1
      },
    ]
  }
}

info = get_from_dict(dictionary, [
  ('age', ['age']),
  ('name', ['name']),
  ('first_grade', ['grades', 0]),
  ('mother', ['family', 'mom']),
  ('early class', ['class', 'schedule', 1]),
  ('late class duration', ['class', 'schedule', 0, 'duration']),
])

print(info)