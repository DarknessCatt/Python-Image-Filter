from flask import Flask, request, send_file
from pyimgfilter import filter as pif
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def main_page():  
  return 'Hello, World!'

@app.route('/image')
def filter_image():
  url = request.args.get('url', default = "https://images.pexels.com/photos/87611/sun-fireball-solar-flare-sunlight-87611.jpeg", type = str)
  radius = request.args.get('radius', default = 10, type = int)

  img = pif(url, radius)

  io = BytesIO()

  mime = ''

  if img.mode in ('RGBA', 'LA'):
  	img.save(io, 'PNG', quality=70)
  	mime = 'image/png'
  else:
  	img.save(io, 'JPEG', quality=70)
  	mime = 'image/jpeg'

  io.seek(0)

  return send_file(io, mimetype=mime)

if __name__ == '__main__':
    app.run(host='0.0.0.0')