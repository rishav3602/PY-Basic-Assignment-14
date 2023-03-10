##  Questions...

"""
1. What does RGBA stand for?
2. From the Pillow module, how do you get the RGBA value of any images?
3. What is a box tuple, and how does it work?
4. Use your image and load in notebook then, How can you find out the width and height of an
Image object?
5. What method would you call to get Image object for a 100×100 image, excluding the lower-left
quarter of it?
6. After making changes to an Image object, how could you save it as an image file?
7. What module contains Pillow’s shape-drawing code?
8. Image objects do not have drawing methods. What kind of object does? How do you get this kind
of object?
"""

## Answers...

"""
1. RGBA stands for Red, Green, Blue, and Alpha. It is a color model used to represent 
colors in an image.

---------------------------------------------------------------------------------------------------

2. To get the RGBA value of an image using the Pillow module, you can use the getpixel() 
method of the Image object. For example, to get the RGBA value of a pixel at position (x,y), 
you can use image.getpixel((x,y)).

---------------------------------------------------------------------------------------------------

3. A box tuple is a tuple that specifies the coordinates of a rectangular region in an image. 
The tuple contains four integers representing the left, upper, right, and lower coordinates 
of the box, in that order. For example, the tuple (100, 100, 200, 200) would represent a box 
with its top-left corner at position (100, 100) and its bottom-right corner at position 
(200, 200).

---------------------------------------------------------------------------------------------------

4. To find out the width and height of an Image object using the Pillow module, you can 
use the size attribute of the Image object. For example, to get the width and height of 
an image stored in the variable img, you can use img.size.

---------------------------------------------------------------------------------------------------

5. To get an Image object for a 100x100 image, excluding the lower-left quarter of it, 
you can use the crop() method of the Image object. For example, to crop an image stored 
in the variable img to exclude the lower-left quarter, you can use img.crop((0, 50, 50, 100)).

---------------------------------------------------------------------------------------------------

6. After making changes to an Image object using the Pillow module, you can save it as an 
image file using the save() method of the Image object. For example, to save an image 
stored in the variable img as a PNG file named output.png, you can use img.save("output.png", 
"PNG").

---------------------------------------------------------------------------------------------------

7. The Pillow module's shape-drawing code is contained in the ImageDraw module.

---------------------------------------------------------------------------------------------------

8.Image objects do not have drawing methods, but the ImageDraw module provides drawing 
methods for drawing shapes and text on images. To get an ImageDraw object, you can use 
the ImageDraw.Draw() function, passing in the Image object you want to draw on as an argument. 
For example, to get an ImageDraw object for an image stored in the variable img, you can 
use draw = ImageDraw.Draw(img).
 

---------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------



"""