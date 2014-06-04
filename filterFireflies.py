#!/bin/python

import Image
import ImageDraw
import os
import sys

if len(sys.argv) != 5:
    print "python filterFireflies.py redThreshold greenThreshold imagesDirectory resultImage"
    sys.exit(1);

redThreshold = float(sys.argv[1])
greenThreshold = float(sys.argv[2])
imagesDirectory = sys.argv[3]
resultImage = sys.argv[4]

print "Red Threshhold:", redThreshold
print "Green Threshhold:", greenThreshold
print "Images Directory:", imagesDirectory
print "Result Image:", resultImage


images = os.listdir(imagesDirectory)
images.sort()

numberOfImages = len(images)
referenceImage = Image.open( os.path.join(imagesDirectory,images[0]) )


newImage = Image.new('RGBA', referenceImage.size, '#000000')

mask=Image.new('L', newImage.size, color=255)
draw=ImageDraw.Draw(mask) 
draw.rectangle((0,0, newImage.size[0], newImage.size[1]), fill=0)
newImage.putalpha(mask)

del referenceImage



for imageIndex in range( 0, numberOfImages ):

    currentImage = Image.open( os.path.join(imagesDirectory,images[imageIndex]) )
    print "Processing Image", imageIndex+1, "of", numberOfImages

    for x in range(0, currentImage.size[0]):
        for y in range(0, currentImage.size[1]):
            redPixel = currentImage.getpixel((x,y))[0]
            greenPixel = currentImage.getpixel((x,y))[1]
            
            #pixelDifference = abs(redPixel - greenPixel) / 255.0
            
            #if redPixel > 50 and greenPixel > 50:# and pixelDifference < 0.1:
            if redPixel > redThreshold and greenPixel > greenThreshold:
				
				currentPixel = currentImage.getpixel((x,y))
				newPixel = list(newImage.getpixel((x,y)))
						
				if newPixel[0] < currentPixel[0]:
					newPixel[0] = currentPixel[0]
				if newPixel[1] < currentPixel[1]:
					newPixel[1] = currentPixel[1]
				
				newImage.putpixel((x,y), tuple(newPixel))
                #newImage.putpixel((x,y), (newImage.getpixel((x,y))[0] + currentImage.getpixel((x,y))[0], newImage.getpixel((x,y))[1] + currentImage.getpixel((x,y))[1],0))
    del currentImage
     
#lastImage = Image.open( os.path.join(imagesDirectory,images[numberOfImages-1]) )      
newImage.save(resultImage, 'JPEG', quality=98)

#lastImage.paste(newImage,(0,0),newImage)
#lastImage.save("Merged.jpg", 'JPEG', quality=98)
