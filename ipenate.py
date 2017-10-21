#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from lxml import html
from requests import get
from re import compile
from colorama import Fore, Style


input = open('main.hyph')
words = input.read().splitlines()
input.close()

words = map(lambda x: compile('\$.*?\$').sub('', x), words)
words = map(lambda x: compile('\W|\d'  ).sub('', x), words)

words = map(lambda x: x.lower(), words)
words = filter(lambda x: x is not '', words)
words = sorted(list(set(words)))

N = len(words)

log_fail = open('ipenate.fail','w')
log_dup = open('ipenate.dup','w')
log_word = open('ipenate.tex','w')
print >>log_word, "\\hyphenation{"

found = []
for i, word in enumerate(words):
  url = 'http://www.merriam-webster.com/dictionary/' + word
  response = get(url)
  tree = html.fromstring(response.content)
  syllables = tree.xpath('normalize-space((//*[@class="word-syllables"])[1]/text())')
  control = syllables.replace(u'·','')
  if control == word and word not in found:
    print "{:>4} su {:>4}: {}{}{}".format(i,N,Fore.GREEN,syllables.encode('utf8'),Style.RESET_ALL)
    print >>log_word, syllables.replace(u'·','-')
    found.append(word)
  elif syllables:
    print "{:>4} su {:>4}: {}{}{}".format(i,N,Fore.YELLOW,word.encode('utf8'),Style.RESET_ALL)
    print >>log_dup, word
  else:
    print "{:>4} su {:>4}: {}{}{}".format(i,N,Fore.RED,word.encode('utf8'),Style.RESET_ALL)
    print >>log_fail, word

print >>log_word, "}"
log_word.close()
log_dup.close()
log_fail.close()
