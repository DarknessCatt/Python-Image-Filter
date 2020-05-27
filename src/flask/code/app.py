from flask import Flask, request, render_template
from pyimgfilter import server_filter as pif
app = Flask(__name__)

@app.route('/')
def main_page():  
  return 'Hello, World!'

@app.route('/image')
def filter_image():
  url = request.args.get('url', default = "https://images.pexels.com/photos/87611/sun-fireball-solar-flare-sunlight-87611.jpeg", type = str)
  radius = request.args.get('radius', default = 10, type = int)

  img = pif(url, radius)
  return img

if __name__ == '__main__':
    app.run(host='0.0.0.0')