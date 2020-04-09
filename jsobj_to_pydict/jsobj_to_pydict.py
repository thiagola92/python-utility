import re
import ast
import json

def convert_to_python(string):
  exceptions = []

  try:
    return convert_using_json_lib(string)
  except Exception as e:
    exceptions.append(e)

  try:
    return convert_using_ast_lib(string)
  except Exception as e:
    exceptions.append(e)

  raise Exception(exceptions)


def convert_using_json_lib(string):
  json_text = re.sub(r'("\s*:\s*)undefined(\s*[,}])', '\\1null\\2', string)

  return json.loads(json_text)

def convert_using_ast_lib(string):
  js_obj = re.sub(r'([\'\"]\s*:\s*)undefined(\s*[,}])', '\\1None\\2', string)
  js_obj = re.sub(r'([\'\"]\s*:\s*)null(\s*[,}])', '\\1None\\2', js_obj)
  js_obj = re.sub(r'([\'\"]\s*:\s*)NaN(\s*[,}])', '\\1None\\2', js_obj)
  js_obj = re.sub(r'([\'\"]\s*:\s*)true(\s*[,}])', '\\1True\\2', js_obj)
  js_obj = re.sub(r'([\'\"]\s*:\s*)false(\s*[,}])', '\\1False\\2', js_obj)

  return ast.literal_eval(js_obj) 