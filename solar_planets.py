import cv2
img=cv2.imread("solar-system.jpg")
print(img)
solar = img[120:360,400:500]
text="SOLAR SYSTEM"
cv2.putText(img,"SOLAR SYSTEM",(300,60),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=3,color=(255,255,255))
cv2.putText(img,"Sun",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(255,255,255))
cv2.putText(img,"Mercury",(100,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Venus",(195,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Moon",(325,160),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(265,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Mars",(380,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Jupiter",(540,90),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Saturn",(740,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Uranus",(950,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Neptune",(1100,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)