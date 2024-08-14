import numpy as np
import cv2
import palette as paltt
import random
import time
start_time = time.time()
def square_mag(v1):
    return (v1[0])**2 + v1[1]**2

image2 = cv2.imread('C:/Users/Storm/Pictures/Saved Pictures/lenna.png')


rows,cols,_ = image2.shape

#palette containing the colours in three channels Y, Cb, Cr
palette = paltt.Palette()

n_of_col = 5

# inpKR = 1
# inpKG = 1
# inpKB = 1
# KR = inpKR/(inpKB+inpKG+inpKR)
# KG = inpKG/(inpKB+inpKG+inpKR)
# KB = inpKB/(inpKB+inpKG+inpKR)
KR = 0.299
KG = 0.587
KB = 0.114

M1 = (
    (0.299,0.587,0.114),
    (-0.16873589164785552,-0.3312641083521444,0.5),
    (0.5,-0.41868758915834514,-0.08131241084165478))

M2 = (
    (1,0,1.4020000000000001),
    (1,-0.34413628620102216,-0.7141362862010223),
    (1,1.772,0))

palette2 = np.array(n_of_col*[0])
for i3 in range(n_of_col):
    x = random.randint(0,len(image2)-1)
    y = random.randint(0,len(image2[:])-1)
    palette2[i3] = image2[x,y,0]

isSorting = True

for yp in range(rows):
    starter_list = []
    ender_list = []
    isSorting = True
    for xp in range(cols):
         
        # image2[yp,xp] = np.add((0,128,128),np.matmul((
        #     (KR,KG,KB),
        #     (-1/2*KR/(1-KB),-1/2 * KG/(1-KB),1/2),
        #     (1/2,-1/2*KG/(1-KR),-1/2*KB/(1-KR)))
        # ,image2[yp,xp]))

        image2[yp,xp] = np.add((0,128,128),np.matmul(M1,image2[yp,xp]))
        
        if isSorting and image2[yp,xp,0] < 100:
            isSorting = False
            starter_list.append(xp)
        elif isSorting == False and image2[yp,xp,0] < 80:
            isSorting = True
            ender_list.append(xp)
    
    # image2[yp] = np.sort(image2[yp],0)
    for i4 in range(len(starter_list)):
        try:
            endcap = ender_list[i4]
        except IndexError:
            endcap = len(image2[yp]) - 1
        image2[yp,starter_list[i4]:endcap] = np.sort(image2[yp,starter_list[i4]:endcap],0)
      


# image2[:,:,1] = 128
# image2[:,:,2] = 128

for yp in range(rows):
    for xp in range(cols):
        
        
        # image2[yp,xp] = np.matmul((
        #     (1,0,2-2*KR),
        #     (1,-KB/KG*(2-2*KB),-KR/KG*(2-2*KR)),
        #     (1,2-2*KB,0)) 
        # ,np.add((0,-128,-128),image2[yp,xp]))        
        image2[yp,xp] = np.matmul(M2,np.add((0,-128,-128),image2[yp,xp]))
        # image2[yp,xp] = np.matmul(M2,image2[yp,xp])


print("--- %s seconds ---" % (time.time() - start_time))
    
    
cv2.imshow("img",image2[:,:,:])
# cv2.imshow("img2",image2[:,:,1])
# cv2.imshow("img3",image2[:,:,2])
    
if cv2.waitKey(0):
    cv2.destroyAllWindows()
   # def set_pixel(local_image, x, y, val):
#     local_image(x,y) = val
