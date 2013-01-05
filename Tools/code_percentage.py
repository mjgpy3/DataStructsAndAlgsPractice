#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jan  3 19:42:26 EST 2013
# 
# 

from pylab import *
from os import popen

figure(2, figsize=(5,5))

lang_to_ext = {'Python': '.py', 'Haskell': '.hs', 'C++': '.cpp',
               'C#': '.cs', 'Ruby': '.rb', 'Java': '.java'}

languages = []
lines = []

for language in lang_to_ext:
    lines.append(int(popen('find /home/michael/Programming/DSAAPractice/ -name "*' + lang_to_ext[language] + '" | xargs nl').readlines()[-1].split()[0]))
    languages.append(language + ': ' + str(lines[-1]))

pie(lines,labels=languages)

savefig('/home/michael/Programming/DSAAPractice/lines_of_code.png')
