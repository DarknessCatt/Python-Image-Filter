import requests
from PIL import Image
from PIL import ImageFilter
import sys

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

  filename = image_url.split("/")[-1]
  r = requests.get(image_url, stream = True)

  if r.status_code == 200:
    print('Image sucessfully retreived: ',filename)

    r.raw.decode_content = True
    im = Image.open(r.raw)

    filtered_img = im.filter(ImageFilter.GaussianBlur(radius=10))

    filtered_img.show()
    
    filtered_img.save(path+filename)
          
  else:
    print('Image Couldn\'t be retreived')

main()