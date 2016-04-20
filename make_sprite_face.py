#Use makeFace(file) function to cut a face from a picture and make an 8-bit sprite face.
#requires OpenCV, Numpy, and Pillow to run.
#Still needs improvment on to fix resizing and cropping issues.
#Works best with an image taken with a webcam at typing distance. 
import cv2
import numpy as np
from PIL import Image

def makeFace(file):#main function
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

	make8bit("face_only.jpg")

####################################################################################
#Extract face using the original image(open with OpenCV), 
#a gray version of that face(also opened with OpenCV, and the coordinates of the face.
#TODO: crop image closer to face.
def extractFG(img,grayImg,x,y,w,h):
	#increase size to fit whole head
	x = x - int(w * 0.15)
	y = y - int(h * 0.15)
	w = w + int(w * 0.15)
	h = h + int(h * 0.25)
	
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

#converts image to an 8-bit color palette, makes the image into blocks that look
#like a classic video game, then scales the image down.
#TODO: finish scale issues
def make8bit(filename):
	convert = 30#blocks that make the image look 8-bit
	resize = 7#devides the image size to be 1/7 of original

	im = Image.open(filename)

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

	#make image smaller(still needs to be improved)
	new = eightbit.resize((eightbit.width/resize,eightbit.height/resize))
	
	new.show()#show for testing
	new.save("eight_bit_face.png","PNG")#save image to a file before return