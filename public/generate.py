from PIL import Image, ImageDraw, ImageOps
from PIL.ImageColor import colormap
import random
import cv2 as cv
import os
import time
import colorsys
import math
from werkzeug.utils import format_string
from collections import deque


image_size_px = 528
padding_px = 100; #can go to half px size


#this is a module, so we don't want to check main
def generate_art(sliderA, sliderB, sliderC, sliderD, sliderE):
        
        print("Generating Art") 
        color = ColorRandomizer()
        image_bg_color = color
        

        dirname = os.path.dirname(__file__)
        timestr = time.strftime("%Y%m%d-%H%M%S")

        imgname = "output_image"+timestr+".png"
        image_path = os.path.join(dirname, r"FlaskRoot\static\images\{}").format(imgname)


        print("GENERATING IMAGE AT: " + image_path) 

        image = Image.new("RGB", size = (image_size_px, image_size_px), color = image_bg_color )
        #draw = ImageDraw.Draw(image) #draw object

        #ueBorder_b = True
        #fill = ColorRandomizer()
        #image = DrawBorder(image, padding_px, fill, ueBorder_b)

        image = DrawFractalFilter(sliderA,sliderB,sliderC, sliderD, sliderE, image_size_px, image);
        #image = TestDrawFractalFilter(image_size_px, image);

        #image = RandomLineDrawerFilter(image_size_px, padding_px, 5, image)
        image.save(image_path)

        imgname = 'static/images/'+imgname

        return imgname


       

def ColorRandomizer():
    
    #rgb
    color = ( RGBRandomInt(),  RGBRandomInt(),  RGBRandomInt())
    return color

def RandomLineDrawerFilter(imagesize, padding, depth, imageObj ):
    draw = ImageDraw.Draw(imageObj) #draw object

    newpoints = []
    for _ in range(depth):

            random_point = ( random.randint(padding, imagesize - padding ), random.randint(padding, imagesize - padding))


            newpoints.append(random_point)
    c = ColorRandomizer()
    for i, point in enumerate(newpoints):
            p1 = point #our point

            if  i == len(newpoints) - 1:
                p2 = newpoints[0]
            else:
                p2 = newpoints[i+1]

                random_point1 = ( random.randint(0, imagesize), random.randint(0, imagesize))
                random_point2 = ( random.randint(0, imagesize), random.randint(0, imagesize))


                line = ( p1, p2 )
               
                line_color = c
                t = 1
                draw.line(line, fill = line_color, width=t)
    return imageObj

# Calculate the mandelbrot sequence for the point c with start value z
def iterate_mandelbrot(c, z = 0):
    for n in xrange(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None

def RandomHSVColor(saturation,brightness, startRange, endRange): #1-360
    #h = random.random()

    h = random.randrange(startRange, endRange)
    h = h / 100
    #print('H after :  ' + str(h))
    float_rgb = colorsys.hsv_to_rgb(h,saturation,brightness)
    rgb = [int(x*255)for x in float_rgb]
    return tuple(rgb)

def NewHSVToRGBColor(h, s, v): #percent
    h = h / 100
    s = s / 100
    v = v / 100
    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x*255)for x in float_rgb]
    return tuple(rgb)


def RGBRandomInt():
    cappedint = random.randrange(0, 255)
    return cappedint

def DrawBorder(imageObj, borderSize, color, useBorder):
     
    if useBorder:
        imageObj = ImageOps.expand(imageObj, border=borderSize, fill= color)


    return image

def DrawFractalFilter(sliderA, sliderB, sliderC, sliderD, sliderE, imgsize, imgOBJ):
    imgx = imgsize; imgy = imgsize
    image = imgOBJ
    draw = ImageDraw.Draw(image) #draw object
    pixels = image.load()
    #print("BEFORE:     Slider a: " + str(sliderA) + "Slider b: " + str(sliderB) + "Slider c: " + str(sliderC) + "Slider d: " + str(sliderD) + "Slider e: " + str(sliderE))
    print("SLIDER E " + str(sliderE)) 
    saturation = sliderC #saturation 0-1
    brightness = sliderD #brightness 0-1
    angle = sliderB/100 #rotation 0-1
    #print("AFTER Slider a: " + str(sliderA) + "Slider b: " + str(r) + "Slider c: " + str(s) + "Slider d: " + str(b) + "Slider e: " + str(sliderE))

    depth = int(sliderA/10) #iterations 1-10
    if depth <= 0:
        depth = 2

    xa = -1.5; xb = 1.5
    ya = -1.5; yb = 1.5
    #n = random.randint(1, depth)  # of spiral arms
    m = random.randint(1, depth) # of spirals in each arm
    n = depth # of spiral arms
    a = 2.0 * math.pi / n     # angle between arms

    b = 2.0 * math.pi * angle # max rotation (bending) angle for each arm
    rmax = 0.1 * random.random() + 0.1 # max spiral radius on each arm
    maxIt = depth # max number of iterations allowed
    # create random color palette
    rd = []; gr = []; bl = []
    points = []

    #base color
    h = random.randint(0, 300)
    h2 = h+50
    col = RandomHSVColor(saturation, brightness, h, h2)



    for c in range(maxIt):

        #t = random.randint(0, 300)
        #t2 = t+50
        #col = RandomHSVColor(1, 1, t, t2)
        
        if (c > 1):
            

            r2 = h + sliderE #color variation
        
            h = random.randint(h + 5, h + r2)
            col = NewHSVToRGBColor(h, saturation, brightness)



        rd.append(col[0])
        gr.append(col[1])
        bl.append(col[2])

    for ky in range(imgy):
        #print(str(100 * ky / (imgy - 1)).zfill(3) + "%")
        for kx in range(imgx):
            x = float(kx) / (imgx - 1) * (xb - xa) + xa
            y = float(ky) / (imgy - 1) * (yb - ya) + ya
            queue = deque([])
            queue.append((x, y, 0))
            
            while len(queue) > 0: # iterate points until none left
                (x, y, i) = queue.popleft()
                if len(queue) == 1:
                    point = (kx,ky)
                    points.append(point)
                
                # apply all (inverse) IFS transformations
                for k in range(n): # of arm
                    for j in range(m): # of a spiral on the arm
                        c = k * a + b * (j + 1.0) / m # angle of the spiral in the arm
                        d = (j + 1.0) / m # distance of the spiral to the center
                        r = d * rmax # radius of the spiral in the arm
                        if r != 0.0:
                            xnew = (x - math.sin(c) * d) / r
                            ynew = (y - math.cos(c) * d) / r
                            
                            if xnew >= xa and xnew <= xb and ynew >= ya and ynew <= yb:
                                if i + 1 == maxIt: break
                                queue.append((xnew, ynew, i + 1))
            #print('I is:  ' + str(i))
            #cc = (rd[i], gr[i], bl[i])
            pixels[kx, ky] = (rd[i], gr[i], bl[i])


    
    return image



               
if __name__ == "__main__": #if being invoked directly (true) else not executed

    generate_art()