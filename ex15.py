from sys import argv        #imports the name of the .py file "ex15.py" & imports one argument

script, filename = argv     #filename = 'Some file the you entered while launching the program' ex - ex15_sample.txt

txt = open(filename)        #sets the contents of 'filename' to 'txt'

print "here's your file %r: " % filename #tells you the file name of 'filename'
print txt.read()            #prints the contents of 'filename'

print "Type the filename again: " #10-15 repeat the process
file_again = raw_input("~>")

txt_again = open(file_again)

print txt_again.read()