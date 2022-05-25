# Author = "Raed Ahsan"
# Date of creation = "25/05/2022"
# Logical Shifting with Python.



a = input("value1: ")
shifting = input('shifting places: ')
opcode = input("what opcode[LSR, LSL]: ")
b = None

a = int(a)
shifting = int(shifting)

if ['LSR','LSL']:
	if opcode == 'LSR':
		b = a >> shifting
		print("Final Value: {}".format(b))
	if opcode == 'LSL':
		b = a << shifting
		print("Final Value: {}".format(b))
