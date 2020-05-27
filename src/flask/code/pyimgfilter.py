import requests
from PIL import Image
from PIL import ImageFilter

image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
filename = image_url.split("/")[-1]

r = requests.get(image_url, stream = True)

if r.status_code == 200:
  print('Image sucessfully retreived: ',filename)

  r.raw.decode_content = True
  im = Image.open(r.raw)

  filtered_img = im.filter(ImageFilter.GaussianBlur(radius=20))

  filtered_img.show()
  
  filtered_img.save(filename)
        
else:
  print('Image Couldn\'t be retreived')