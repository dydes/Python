pip install removebg
from removebg import RemoveBg

#获取API
rmbg = RemoveBg("xrCqrD4fee1fGhej3yzDGAmc", "error.log") 

#图片地址
rmbg.remove_background_from_img_file("D:\会通\9.没事PS\timg.jpg")