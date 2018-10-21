#!/usr/bin/env python

import csv

def createDemoDict():
  demo_dict = [
    {"key1": 01, "key2": 02, "key3": 03},
    {"key1": 11, "key2": 12, "key3": 13},
    {"key1": 21, "key2": 22, "key3": 23}
  ]
  return demo_dict

def csvToDictList(csv_filename, **kwargs):
  sep=','
  arrayList = []
  if("separator" in kwargs):
    sep=kwargs['separator']
  with open(csv_filename) as csvfile:
       reader = csv.DictReader(csvfile, delimiter=sep, quoting=csv.QUOTE_NONE)
       arrayList=list(reader)
       #for row in reader:
       #    arrayList.append(row)
  return arrayList


def dictListToCsv(dictList, csv_filename, **kwargs):
  sep=','
  if("separator" in kwargs):
    sep=kwargs['separator']
  keys = dictList[0].keys() # only first dict keys are needed, we assume all others are the same
  with open(csv_filename, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter=sep, quoting=csv.QUOTE_NONE)
    dict_writer.writeheader()
    dict_writer.writerows(dictList)

# Main function definition
def main():
  dictListToCsv(createDemoDict(), "test.csv", separator="_" )
  print(csvToDictList("test.csv", separator="_" ))
if __name__== "__main__":
  main()
