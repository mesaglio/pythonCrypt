import sys
import random
import hashlib

def change_ascii(char,aux):
	return chr(ord(char)+aux)

def restore_ascii(char,aux):
	return chr(ord(char)-aux)

def code(file):
	num = ''
	_read = ord(file.read(1))
	while  _read != 32:
		num += chr(_read)
		_read = ord(file.read(1))
	for x in range(1,101):
		x_str = str(x)
		if hashlib.md5(x_str.encode()).hexdigest() == num:
			return x

def execute_ok():
	if len(sys.argv) != 3:
		print("Cantidad incorrect de argumentos")
		sys.exit(0)
	else:
		print("Cantidad correcta de argumentos")

def crypt():
	print("Encriptando...")	
	file_crypt = open("encriptado.crypt","w")
	file_to_read = open(sys.argv[2],"r")
	time = random.randint(1,101)
	time_string = str(time)
	time_hash = hashlib.md5(time_string.encode()).hexdigest()
	file_crypt.write(time_hash)
	file_crypt.write(' ')
	for line in file_to_read:
		for char in line:
			file_crypt.write(change_ascii(char,time))

def decrypt():
	print("Desencriptando...")	
	file_write = open("archivoOriginal.txt","w")
	file_to_read = open(sys.argv[2],"r")
	time = code(file_to_read)
	for line in file_to_read:
		for char in line:
			file_write.write(restore_ascii(char,time))

def main():
	execute_ok()
	if sys.argv[1] == "1":
		crypt()
	if sys.argv[1] == "2":
		decrypt()

main()
