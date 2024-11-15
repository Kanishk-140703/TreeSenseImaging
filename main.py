from flask import Flask, request, render_template 
from image_processing import ImageSeg, OptimalPathing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_image():
  if request.method == 'POST':
    # Get uploaded image
    image_file = request.files['imageInput']
    # Process image and calculate path
    img_seg = ImageSeg(image_file.read())
    processed_image, path = OptimalPathing(img_seg.IsoGrayThresh(), 'path/to/target_image.jpg').ComputeDjikstra()
    # Return processed image data URL or path (adjust based on your needs)
    return render_template('index.html', processed_image=processed_image)  # Assuming processed_image is a data URL
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)