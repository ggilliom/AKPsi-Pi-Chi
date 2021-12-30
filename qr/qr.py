import qrcode
from PIL import Image # $ pip install pillow

# Should be able to do this with pandas instead to avoid manual text file edits

def getFileLines(file): # returns lines of a file in list form
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

def fileStuff(name): # Pass in file name, return lines of that file
	fileName = name
	file = open(fileName, "r")
	lines = getFileLines(file)
	file.close()
	return lines


firsts = fileStuff("firsts.txt")
lasts = fileStuff("lasts.txt")
majors = fileStuff("majors.txt")
towns = fileStuff("towns.txt")

# Loop through lists together to form qrcodes
for first, last, major, town in zip(firsts, lasts, majors, towns):
	print(first + " " + last)

	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_H,
	    box_size=10,
	    border=4,
	)
	# this string stuff is gross but...................im too lazy to fix it
	qr.add_data(first + " " + last + "\n" + major + "\n" + town)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

	img.save("qrcodes/" + first + last + ".png")

print("Done! QR codes saved in local 'qrcodes' directory.")
