#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

#1
def grayscale(pixels):
    """The blan-image returned value is saved in a variable, the using a nested loop, in each itteration,
 a value from the 2D list is assigned to an instance of that value."""
    height=len(pixels)
    width=len(pixels[0])
    green_pic=blank_image(height, width)
    for r in range(height):
        for c in range(width):
            green_pic[r][c]=[brightness(pixels[r][c]),brightness(pixels[r][c]),brightness(pixels[r][c])] 
    return green_pic 

#2
def fold_diag(pixels):
    """Same algorithm as #1 plus added if conditions"""
    height=len(pixels)
    width=len(pixels[0])
    green_pic=blank_image(height, width)
    for r in range(height):
        for c in range(width):
            if r>c:
                green_pic[r][c]=[255,255,255]
            else:
                green_pic[r][c]=pixels[r][c]
    return green_pic

#3
def mirror_horiz(pixels):
    """after the middle index, for every c we have to returm a value from
middle back to 0"""
    middle=len(pixels[0])//2
    height=len(pixels)
    width=len(pixels[0])
    green_pic=blank_image(height, width)
    for r in range(height):
        for c in range(width):
            if c<middle:
                green_pic[r][c]=pixels[r][c]               
            else:
                green_pic[r][c]=pixels[r][width-(c+1)]
    return green_pic

#4
def extract(pixels, rmin, rmax, cmin, cmax):
    """Using the input variables and nested loops, the picture is extracted."""
    h=len(pixels[rmin:rmax])
    w=len(pixels[0][cmin:cmax])
    green_pic=blank_image(h,w)

    for r in range(h):
        for c in range(w):
            green_pic[r][c]=pixels[rmin][(cmax+c)-(cmax-cmin)]
        rmin+=1
        
    return green_pic          
    


                
                
      



