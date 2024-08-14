import numpy as np
import cv2
import Floater_File as ff

def square_mag(v1):
    return (v1[0])**2 + v1[1]**2

pos = np.array((.5,.5))



#try?
image_size_inp = int(input("image resolution: "))
image_size = image_size_inp

obj1 = ff.Floater((0.5*image_size,0.5*image_size), 0)

obj1.rotate(np.pi/4)
obj1.move(20)

image = np.array([[[0] * 3] * image_size] * image_size, dtype = np.uint8)

rows,cols,_ = image.shape

closest_pixel = (int(pos[0] * image_size),int(pos[1]* image_size))


image[closest_pixel[0],:,0] = 255
image[:,closest_pixel[1],1] = 255
image[closest_pixel] = (0,0,255)

# for yp in range(rows):
#     for xp in range(cols):
#         if square_mag((xp,yp)-pos*image_size) < 200:
#             image[xp,yp] = (255,255,255)
i=0
while True:
    i += 1

    obj1.rotate(np.pi*.05)
    obj1.move(20)

    for yp in range(rows):
        for xp in range(cols):
            if square_mag((xp,yp) - obj1.location) < 40:
                image[xp,yp] = (255,255,255)
    
    
    
    cv2.imshow("img",image)
    
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
# def set_pixel(local_image, x, y, val):
#     local_image(x,y) = val
