from jsobj_to_pydict import convert_to_python

f = open("big_test.js", 'r')
string = f.read()
f.close()

py_dict = convert_to_python(string)
print(py_dict)