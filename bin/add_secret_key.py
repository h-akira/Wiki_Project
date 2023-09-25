#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-09-25 13:54:09

import sys
import os
import numpy

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\
settings_local_sample.pyを読み込み，\
生成したSECRET_KEYを追記してsettings_local.pyとして出力する．
""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("-s", "--sample", metavar="settings-sample-file", default="settings_local_sample.py", help="SECRET_KEYを設定しているファイルのサンプル")
  parser.add_argument("-o", "--output", metavar="output-file", default="settings_local.py", help="output file")
  parser.add_argument("-p", "--print", action="store_true", help="SECRET_KEYをprintする")
  options = parser.parse_args()
  return options

def main():
  options = parse_args()
  from django.core.management.utils import get_random_secret_key
  key = get_random_secret_key()
  if options.print:
    print("---- SECRET_KEY ----")
    print(key)
    print("--------------------")
  if os.path.isfile(options.sample):
    with open(options.sample, mode="r") as f:
      text = f.read()
    if "SECRET_KEY = 'django-insecure-{}'" not in text:
      print("`SECRET_KEY = django-instance-{}` is not exists. Add this to the end?")
      if "y" == input("入力(y/other):"):
        text += "SECRET_KEY = 'django-insecure-{}'\n".format(key)
      else:
        print("Exit without saving.")
        sys.exit()
    else:
      text = text.replace(
        "SECRET_KEY = 'django-insecure-{}'",
        "SECRET_KEY = 'django-insecure-{}'".format(key)
      )
    if os.path.isfile(options.output):
      print(f"`{options.output}` already exists. Overwrite this file?")
      if "y" != input("Please enter 'y' or something else:"):
        print("Exit without saving.")
        sys.exit()
    with open(options.output, mode="w") as f:
      f.write(text)
      print(f"Wrote to `{options.output}`.")
  else:
    print(f"`{options.sample}` is not exists.")


if __name__ == '__main__':
  main()
