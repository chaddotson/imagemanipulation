#!/bin/python

import Image
import ImageDraw
import os
import sys

if len(sys.argv) != 5:
    print "python overlay.py imagesDirectory resultImage"
    sys.exit(1);

resultImage = sys.argv[2]

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
            current_pixel = currentImage.getpixel((x,y))
            print current_pixel
        #		newImage.putpixel((x,y), tuple(newPixel))
                #newImage.putpixel((x,y), (newImage.getpixel((x,y))[0] + currentImage.getpixel((x,y))[0], newImage.getpixel((x,y))[1] + currentImage.getpixel((x,y))[1],0))
    del currentImage
     
#lastImage = Image.open( os.path.join(imagesDirectory,images[numberOfImages-1]) )      
#newImage.save(resultImage, 'JPEG', quality=98)

