import numpy as np
import cv2
import Floater_File as ff

def square_mag(v1):
    return (v1[0])**2 + v1[1]**2

#pos = np.array((.5,.5))



#try?
# image_size_inp = int(input("image resolution: "))
# image_size = image_size_inp

# obj1 = ff.Floater((0.5*image_size,0.5*image_size), 0)

# obj1.rotate(np.pi/4)
# obj1.move(20)

# image = np.array([[[0] * 3] * image_size] * image_size, dtype = np.uint8)

image2 = cv2.imread('C:/Users/Storm/Pictures/Saved Pictures/lenna.png')


rows,cols,_ = image2.shape

#closest_pixel = (int(pos[0] * image_size),int(pos[1]* image_size))


# image[closest_pixel[0],:,0] = 255
# image[:,closest_pixel[1],1] = 255
# image[closest_pixel] = (0,0,255)

# # for yp in range(rows):
#     for xp in range(cols):
#         if square_mag((xp,yp)-pos*image_size) < 200:
#             image[xp,yp] = (255,255,255)

M1 = (
    (0.2126,0.7152,0.0722),
    (-0.1146,-0.3854,0.5),
    (0.5,-0.4542,-0.0458))

M2 = (
    (1,0,1.5748),
    (1,-0.1873,-0.4681),
    (1,1.8556,0))

inpKR = 1
inpKG = 1
inpKB = 1
KR = inpKR/(inpKB+inpKG+inpKR)
KG = inpKG/(inpKB+inpKG+inpKR)
KB = inpKB/(inpKB+inpKG+inpKR)
# KR = 0.299
# KG = 0.587
# KB = 0.114


for yp in range(rows):
    for xp in range(cols):
         
        image2[yp,xp] = np.add((0,128,128),np.matmul((
            (KR,KG,KB),
            (-1/2*KR/(1-KB),-1/2 * KG/(1-KB),1/2),
            (1/2,-1/2*KG/(1-KR),-1/2*KB/(1-KR)))
        ,image2[yp,xp]))
        # image2[yp,xp] = np.matmul(M1,image2[yp,xp])

# image2[:,:,0] = 128
# image2[:,:,1] = 128

for yp in range(rows):
    for xp in range(cols):
        
        
        image2[yp,xp] = np.matmul((
            (1,0,2-2*KR),
            (1,-KB/KG*(2-2*KB),-KR/KG*(2-2*KR)),
            (1,2-2*KB,0)) 
        ,np.add((0,-128,-128),image2[yp,xp]))
        # image2[yp,xp] = np.matmul(M2,image2[yp,xp])



    
    
cv2.imshow("img",image2[:,:,:])
# cv2.imshow("img2",image2[:,:,1])
# cv2.imshow("img3",image2[:,:,2])
    
if cv2.waitKey(0):
    cv2.destroyAllWindows()
   # def set_pixel(local_image, x, y, val):
#     local_image(x,y) = val
