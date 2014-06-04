import Image
import os
import sys


steps=5




imagesDirectory = sys.argv[1]


print "Images:" + imagesDirectory

images = os.listdir(imagesDirectory)
images.sort()

numberOfImages = len(images)

for imageIndex in range( 0, numberOfImages-1 ):
	image1Name = os.path.splitext(os.path.basename( images[imageIndex] ))[0]
	image2Name = os.path.splitext(os.path.basename( images[imageIndex+1]))[0]
	
	
	
	image1 = Image.open( os.path.join(imagesDirectory,images[imageIndex]) )
	image2 = Image.open( os.path.join(imagesDirectory,images[imageIndex+1]) )
	
	for i in range(0,steps-1):
		newImage = Image.new('RGBA', (1626, 1080), '#000000')
		newImageName = os.path.join( imagesDirectory, image1Name ) +"_" + str(i+1) + ".jpg"
	
		blendPercent = float(float(i+1)/float(steps))
	
		print image1Name + "+" + image2Name + "=>" + os.path.basename(newImageName),i,steps,blendPercent
		#print i,steps,blendPercent
	
		
		for y in range(0,1080):
			for x in range(0,1626):
				#print x, y
				originalPixel1 = image1.getpixel((x,y))
				originalPixel2 = image2.getpixel((x,y))
					
				
				newPixel = [0,0,0]
				
				newPixel[0] = int((1.0-blendPercent) * originalPixel1[0] + blendPercent * originalPixel2[0])
				newPixel[1] = int((1.0-blendPercent) * originalPixel1[1] + blendPercent * originalPixel2[1])
				newPixel[2] = int((1.0-blendPercent) * originalPixel1[2] + blendPercent * originalPixel2[2])
				
				
				#pixel = (1.0-blendPercent) * image1.getpixel((x,y)) + blendPercent * image2.getpixel((x,y))
			
				newImage.putpixel((x,y),(newPixel[0],newPixel[1],newPixel[2]))
		newImage.save(newImageName, 'JPEG', quality=98)
	
	

sys.exit(1)


	
image1Name = "0001"
image2Name = "0002"
image1 = Image.open( image1Name + ".jpg" )
image2 = Image.open( image2Name + ".jpg" )

for i in range(0,steps):
	newImage = Image.new('RGBA', (1626, 1080), '#000000')
	
	blendPercent = float(float(i)/float(steps))
	
	print i,steps,blendPercent
	
	for y in range(0,1080):
		for x in range(0,1626):
			#print x, y
			originalPixel1 = image1.getpixel((x,y))
			originalPixel2 = image2.getpixel((x,y))
				
			
			newPixel = [0,0,0]
			
			newPixel[0] = int((1.0-blendPercent) * originalPixel1[0] + blendPercent * originalPixel2[0])
			newPixel[1] = int((1.0-blendPercent) * originalPixel1[1] + blendPercent * originalPixel2[1])
			newPixel[2] = int((1.0-blendPercent) * originalPixel1[2] + blendPercent * originalPixel2[2])
			
			
			#pixel = (1.0-blendPercent) * image1.getpixel((x,y)) + blendPercent * image2.getpixel((x,y))
		
			newImage.putpixel((x,y),(newPixel[0],newPixel[1],newPixel[2]))
	newImage.save(image1Name + "_" + str(i) + ".jpg")

			
	