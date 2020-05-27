import requests
from PIL import Image
from PIL import ImageFilter
import sys
from io import BytesIO
from flask import send_file

def help():
  print("Script Usage:")
  print("python3", sys.argv[0], "<URL> <radius> <path>")
  print("<URL> = Image's URL")
  print("<radius> = GaussianBlur's radius")
  print("<path> = Image's save path (default: \'./\' ")
  sys.exit(2)

def main():

  if len(sys.argv) < 3:
    help()

  image_url = sys.argv[1]
  blur_radius = int(sys.argv[2])
  path = "./"

  if sys.argv[3] is not None:
    path = sys.argv[3]

  img = filter(image_url, blur_radius, path)

  if img is not None:
    img.show() 
    img.save(path+filename)
  
def filter(url, radius, path="./"):
  filename = url.split("/")[-1]
  r = requests.get(url, stream = True)

  if r.status_code == 200:
    print('Image sucessfully retreived: ',filename)

    r.raw.decode_content = True
    im = Image.open(r.raw)

    filtered_img = im.filter(ImageFilter.GaussianBlur(radius))

    return filtered_img
          
  else:
    print('Image Couldn\'t be retreived')

    return None

def server_filter(url, radius, path="./"):
    img = filter(url, radius, path)
    io = BytesIO()
    img.save(io, 'JPEG', quality=70)
    io.seek(0)
    return send_file(io, mimetype='image/jpeg')