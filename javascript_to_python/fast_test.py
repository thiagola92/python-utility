from javascript_to_python import convert_to_python

string = """{
  "nome": "Thiago",
  "idade": 27,
  "nota": 9.8,
  "livros": {
    "sim": 1,
    "nao": 2
  },
  "limite": NaN,
  "undefined":undefined,
  "undefined":   undefined,
  "undefined":   \nundefined,
  "undefined":   \n\t\rundefined,
  "undefined":"undefined",
  "undefined"  :  "espaços em ambos os lados tem q ser valido",
  "undefined":"a descrição do produto pode ter a palavra undefined kkk",
  "undefined":"tem que tomar cuidado com alguém tentando reproduzir nosso regex então \\":undefined,",
  "undefined":undefined
}"""

py_dict = convert_to_python(string)
print(py_dict)