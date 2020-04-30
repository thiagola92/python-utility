# deep-get
Used to get data from unknown structures.  

# usage
**data**

```python
json = {
  "name": "thiago",
  "age": 18,
  "classes": [
    {
      "name": "introduction to computer science",
      "professor": "ivan",
      "grade": [
        9,
        5,
        3
      ]
    },
    {
      "name": "programming 1",
      "professor": "noemi",
      "grade": [
        10,
        8
      ]
    }
  ]
}

dget(json, ["name"]) # "thiago"
dget(json, ["classes", 0, "professor"]) # ivan
dget(json, ["classes", 1, "professor"]) # noemi
dget(json, ["classes", 1, "grade", 0]) # 10
dget(json, ["classes", 1, "grade", 2]) # None
dget(json, ["classes", 1, "grade"]) # [10, 8]
dget(json, ["classes", 0, "grade"]) # [9, 5, 3]
dget(json, ["classes", 0]) # {"name": "introduction to computer science", "professor": "ivan", "grade": [9,5,3]}
dget(json, ["name", 2]) # 'i'
```