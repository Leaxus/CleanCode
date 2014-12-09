import os
import getopt, sys

def usage():
  print("""Usage: mkproj [OPTIONS]
    -m language       Create a Makefile for the language
    -a                Create the AUTHORS file
    -d                Create TODO and README""")

try:
  opts, args = getopt.getopt(sys.argv[1:], "m:ad")
except getopt.GetoptError as err:
  usage()
  sys.exit(2)

for o, a in opts:
  if o == "-a":
    AUTHORS = open('AUTHORS', 'w')
    AUTHORS.write('* phones_a\n')
    AUTHORS.close()
  elif o == "-d":
    TODO = open('TODO', 'w')
    TODO.write(''' ______  _____   ____    _____
/\__  _\/\  __`\/\  _`\ /\  __`\\
\/_/\ \/\ \ \/\ \ \ \/\ \ \ \/\ \\
   \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\
    \ \ \ \ \ \_\ \ \ \_\ \ \ \_\ \\
     \ \_\ \ \_____\ \____/\ \_____\\
      \/_/  \/_____/\/___/  \/_____/

 _______________________________________________
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|_______________________________________________|''')
    TODO.close()
    README = open('README', 'w')
    README.write(''' ____    ____    ______  ____             ____
/\  _`\ /\  _`\ /\  _  \/\  _`\   /'\_/`\/\  _`\\
\ \ \L\ \ \ \L\_\ \ \L\ \ \ \/\ \/\      \ \ \L\_\\
 \ \ ,  /\ \  _\L\ \  __ \ \ \ \ \ \ \__\ \ \  _\L
  \ \ \\\\ \\\\ \ \L\ \ \ \/\ \ \ \_\ \ \ \_/\ \ \ \L\ \\
   \ \_\ \_\ \____/\ \_\ \_\ \____/\ \_\\\\ \_\ \____/
    \/_/\/ /\/___/  \/_/\/_/\/___/  \/_/ \/_/\/___/

DESCRIPTION

AUTHORS
    Alex Phonesavanh <phones_a> alias Leaxus
    <alex.phonesavanh@epita.fr>''')
    README.close()
  elif o == "-m":
    Makefile = open('Makefile', 'w')
    if a == "c":
      Makefile.write("CC=gcc\nCFLAGS=-Wall -Wextra -Werror -std=c99 -pedantic\n\nall:\n\nclean:")
    elif a == "cpp":
      Makefile.write("CXX=clang++\nCXXFLAGS=-Wall -Wextra -Werror -std=c++1y -pedantic\n\nall:\n\nclean:")
    Makefile.close()
