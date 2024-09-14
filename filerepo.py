import os
os.mkdir('testdir')

file = open('testdir/example.txt', 'w')
lines = ('This\n is\n a\n line\n')
file.write(lines)
file.close()