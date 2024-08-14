import numpy as np
import cv2
import palette as paltt

def square_mag(v1):
    return (v1[0])**2 + v1[1]**2

image2 = cv2.imread('C:/Users/Storm/Pictures/Saved Pictures/lenna.png')


rows,cols,_ = image2.shape

#palette containing the colours in three channels Y, Cb, Cr
palette = paltt.Palette()

n_of_col = 10

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

        
        i = 0
        for col in image2[yp,xp]:
            
            i2 = 0
            #find location in stack

            while col >= palette.colors[i2] and col >= palette.colors[i2+1]:
                i2+=1
            
            #check both distances SHOULD BE NOT INCLUDING THE COMPETING COLOR
            if palette.shortest_dist > np.abs(col - palette.colors[i2]):
                palette.add_color(col,i2, True)
            elif palette.shortest_dist > np.abs(col - palette.colors[i2+1]):
                palette.add_color(col,i2, False)   


            if len(palette.colors) >= n_of_col:            
                palette.add_color(col,i2, None)
            
            i+=1


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
