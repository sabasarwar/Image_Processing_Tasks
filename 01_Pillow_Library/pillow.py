from PIL import Image
img_01 = Image.open("flower_01.jpg")
print("Type of image: ", type(img_01))
print("Mode of image: ", img_01.mode)
print("Size of image: ", img_01.size)
#Resize the original image and save it, will resize(squeeze) but won't crop
small_img = img_01.resize((500,500))
small_img.save("flower_02.jpg")
print("Type of image: ", type(small_img))
print("Mode of image: ", small_img.mode)
print("Size of image: ", small_img.size)
#Resize with cropping the original image using thumbnail function
img_01.thumbnail((400,500))
img_01.save("flower_03.jpg")
print("Type of image: ", type(img_01))
print("Mode of image: ", img_01.mode)
print("Size of image: ", img_01.size)
#Crop image using crop()
cropped_img = img_01.crop((0,0,300,300))
cropped_img.save("flower_04.jpg")
print("Size of image: ",cropped_img.size)
#To copy and paste an image over another image : use copy(), paste()
#Image rotation: keeping aspect ratio of original image
#Rotate image by 45
img45 = img_01.rotate(45)
img45.save("flower_45.jpg")

#Image rotation, completeley rotate
img50 = img_01.rotate(50, expand=True)
img50.save("flower_50.jpg")
#Flip and Transpose of image
#Flip from left to right
img_02 = Image.open("cat_01.jpg")
img_flipR = img_02.transpose(Image.FLIP_LEFT_RIGHT)
img_flipR.save("cat_02.jpg")

#Flip from top to bottom
img_02 = Image.open("cat_01.jpg")
img_flipT = img_02.transpose(Image.FLIP_TOP_BOTTOM)
img_flipT.save("cat_03.jpg")
#Change image to grayscale
img_03 = Image.open("multi_01.jpg")
grey_img = img_03.convert("L")
grey_img.save("multi_02.jpg")
# https://pillow.readthedocs.io/en/stable/reference/Image.html


#To automate image processing for multiple images.

from PIL import Image
import glob

path = "img/aeroplane/*.*"
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    a= Image.open(file)  #now, we can read each file since we have the full path

    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png", "PNG")
