#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from lxml import html
import requests

input = open('en-hyphens.hyph')
words = input.read().splitlines()
N = len(words)
input.close()

output = open('en-ipenate.tex','w')
unresol = open('en-ipenate.unres', 'w')

print >>output, '\\hyphenation{'
for i, word in enumerate(words):
  url = 'http://www.merriam-webster.com/dictionary/' + word
  response = requests.get(url)
  tree = html.fromstring(response.content)
  syllables = tree.xpath('normalize-space((//*[@class="word-syllables"])[1]/text())')
  if syllables:
    print str(i+1)+"\tsu\t"+str(N)+"\t \t"+syllables
    print >>output, syllables.replace(u'·','-')
    output.flush()
  else:
    print >>unresol, word
    print str(i+1)+"\tsu\t"+str(N)+"\tX\t"+word
    unresol.flush()
print >>output, '}'

output.close()
unresol.close()
