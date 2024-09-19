#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2024-09-19 21:44:15

import sys
import os
import json

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(description="""\

""", formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--version", action="version", version='%(prog)s 0.0.1')
  parser.add_argument("-o", "--output", metavar="output-directory", default="OUTPUT", help="output directory")
  # parser.add_argument("-", "--", action="store_true", help="")
  # parser.add_argument("file", metavar="input-file", help="input file")
  options = parser.parse_args()
  if not os.path.isfile(options.file): 
    raise Exception("The input file does not exist.") 
  return options

def main():
  options = parse_args()
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Wiki_Project.settings")
  import django
  django.setup()
  from django.conf import settings
  from Wiki.models import PageTable
  for i, page in enumerate(PageTable.objects.all()):
    dic = {
      "username": page.user.username,
      "last_updated": page.last_updated,
      "slug": page.slug,
      "priority": page.priority,
      "title": page.title,
      "public": page.public,
      "edit_permission": page.edit_permission,
      "share": page.share,
      "share_edit_permission": page.share_edit_permission,
      "share_code": page.share_code,
      "text": page.text
    }
    with open(os.path.join(options.output, f"{i:04}.json"), "w") as f:
      json.dump(dic, f, indent=2)

if __name__ == '__main__':
  main()
