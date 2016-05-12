#Use makeFace(file) function to cut a face from a picture and make an 8-bit sprite face.
#requires OpenCV, Numpy, and Pillow to run.
#Still needs improvment on to fix resizing and cropping issues.
#Works best with an image taken with a webcam at typing distance. 
#this file is a mess right now
import cv2
import numpy as np
from PIL import Image

def makeSprite(faceFile, spriteFile, newSpriteFile):
	headless = Image.open(spriteFile)#file with the sprite that does not have a face yet.
	
	#find red square
	xIndex = 0
	yIndex = 0
	for y in range(headless.height):
		if(yIndex > 0):
			break
		for x in range(headless.width):
			if(xIndex > 0):
				break

			pixel = headless.getpixel((x,y))

			if(pixel[0] > 150 and pixel[1] < 80 and pixel[2] < 80):
				xIndex = x 

				while(pixel[0] > 150 and pixel[1] < 80 and pixel[2] < 80):
					x = x + 1
					pixel = headless.getpixel((x,y))

				x = x - 1#go back to to red square
				w = x - xIndex#calculate width 

				pixel = headless.getpixel((x,y))
				yIndex = y
				while(pixel[0] > 150 and pixel[1] < 80 and pixel[2] < 80):
					y = y + 1
					pixel = headless.getpixel((x,y))

				y = y - 1#go back to red square
				h = y - yIndex

	faceOnlyFile = makeFace(faceFile)

	eightBitFace =  make8bit(faceOnlyFile,(w + 3,h + 2))

	#face = face.resize((w + 3,h + 2))

	eightBitFace = eightBitFace.convert("RGBA")

	eightBitFace = fixEdges(eightBitFace) 

	headless.paste(eightBitFace,(xIndex - 1,yIndex - 1))

	headless.save(newSpriteFile,'png')


def fixEdges(image):
	width, height = image.size
	changes = image.load()
	for y in range(height):
		for x in range(width):
			pixel = image.getpixel((x,y))
			if(pixel[0] < 8 and pixel[1] < 8 and pixel[2] < 8):
				changes[x,y] = (255,255,255,0)
	return image




def makeFace(file):
	#set up face detection
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	im = cv2.imread(file)
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	
	#find the lagest face
	largest = faces[0]
	for i in faces:
		if(i[2] * i[3] > largest[2] * largest[3]):#[x,y,w,h]
			largest = i



	#get the face from the image 
	face_only = extractFG(im,gray,largest[0],largest[1],largest[2],largest[3])

	#write to a file before opening with Pillow
	cv2.imwrite("face_only.jpg",face_only)

	return "face_only.jpg"

####################################################################################
#Extract face using the original image(open with OpenCV), 
#a gray version of that face(also opened with OpenCV, and the coordinates of the face.
#TODO: crop image closer to face.
def extractFG(img,grayImg,x,y,w,h):
#	increase size to fit whole head
#	x = x - int(w * 0.15)
#	y = y - int(h * 0.15)
#	w = w + int(w * 0.15)
#	h = h + int(h * 0.25)
	
	rect = (x,y,w,h) #Region Of Interest

	#set up for grabcut
	mask = np.zeros(img.shape[:2],dtype = np.uint8)
	bgdmodel = np.zeros((1,65),np.float64)
	fgdmodel = np.zeros((1,65),np.float64)

	#find eyes
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	roi_gray = grayImg[y:y+h,x:x+w]
	roi_mask = mask[y:y+h,x:x+w]#set up parallel roi
	eyes = eye_cascade.detectMultiScale(roi_gray)

	#first cut without marking eyes as foreground
	cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,1,cv2.GC_INIT_WITH_RECT)
	
	#mark eyes
	for(ex,ey,ew,eh) in eyes:
		eh = eh + (int(eh) * 2)
		cv2.rectangle(roi_mask,(ex,ey),(ex+ew,ey+eh),1,-1)

	#second cut with eyes marked as foreground	
	cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,1,cv2.GC_INIT_WITH_MASK)

	#get output from original picture and mask
	mask2 = np.where((mask==1) + (mask == 3),255,0).astype('uint8')
	output = cv2.bitwise_and(img,img,mask=mask2)
	output = output[y:y+h,x:x+w]#cropping needs improvment



	return output#return a picture with a black background and a face.
################################################################################
#takes in an image (open with OpenCV) and crops the (0,0,0) edges off. 
#returns 
#def cropSides(image):

################################################################################
#converts image to an 8-bit color palette, makes the image into blocks that look
#like a classic video game, then scales the image down.
#TODO: finish scale issues
def make8bit(filename,size):
	convert = 5#blocks that make the image look 8-bit

	im = Image.open(filename)

	im = im.resize(size)

	#im = im.filter(ImageFilter.MedianFilter(size=7))

	#convert to an 8-bit color palette
	eightbit = im.convert("P",palette=Image.ADAPTIVE,colors=256)

	width, height = eightbit.size
	
	pixels = []#set up empty list to hold pixels
	changes = eightbit.load()#access pixels 

	#make blocks
	for x in range(0,width - convert,convert):
		for y in range(0,height - convert,convert):	
			pixels = []
			for i in range(x,x+convert):
				for j in range(y,y+convert):
					pixels.append(eightbit.getpixel((i,j)))
			pixels.sort()
			#avg = sum(pixels) / len(pixels)
			for i in range(x,x+convert):
				for j in range(y,y+convert):
					changes[i,j] = pixels[(convert ** 2) / 2]
					#changes[i,j] = avg
	
	#new.show()#show for testing
	#new.save("eight_bit_face.png","PNG")#save image to a file before return
	return(eightbit)