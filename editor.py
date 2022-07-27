# from PIL import Image
# from PIL import ImageFilter
 
# with Image.open("photo.jpg") as image_file:
#     print("Size:", image_file.size)
#     print("Format:", image_file.format)
#     print("Type:", image_file.mode)
#     image_file.show()
 
# with Image.open("photo.jpg") as pic_original:
#     pic_gray = pic_original.convert("L") #chinh sang dang trang den
#     pic_gray.save("photo1.jpg")#luu file
#     #pic_gray.show()
 
#     pic_up = pic_gray.tranpose(Image.ROTATE_90)#xoay file hinh
#     pic_up.save("photo2.jpg")#luu file
from PIL import Image
from PIL import ImageFilter
class ImageEditor():
    def __init__(self, file_name):
        self.filename = file_name #ten
        self.original = None #file goc
        self.changed = list() #su thay doi
    def open(self):
            try:
                self.original = Image.open(self.filename)#mo file dong thoi luu vao bien original
            except:
                print("File not found!")
            self.original.show()#hien original ra
    
    def rotate_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT) #xoay file 
        self.changed.append(rotated) #them vao bien thay doi
 
        current_file_name = self.filename.split(".") # ["photo", "jpg"]
        #               photo1.jpg
        new_file_name = current_file_name[0] + str(len(self.changed)) + ".jpg"
        rotated.save(new_file_name)
    
    def crop(self):
        #trai tren phai duoi
        box = (250, 100, 600, 400) #left, up, right, down
        cropped = self.original.crop(box) #thuc hien cat tam hinh theo kick theo co o tren
        self.changed.append(cropped)
        current_file_name = self.filename.split(".") # ["photo", "jpg"]
        #               photo1.jpg
        new_file_name = current_file_name[0] + str(len(self.changed)) + ".jpg"
        cropped.save(new_file_name)
    def blur(self):
        blured = self.original.filter(ImageFilter.BLUR)
        self.changed.append(blured)
        current_file_name = self.filename.split(".") # ["photo", "jpg"]
        #               photo1.jpg
        new_file_name = current_file_name[0] + str(len(self.changed)) + ".jpg"
        blured.save(new_file_name) 
 
my_Editor = ImageEditor("photo.jpg")
my_Editor.open()
my_Editor.rotate_left()
my_Editor.crop()
my_Editor.blur()
 

