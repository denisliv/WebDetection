import os
import cv2
from flask import Flask, render_template, request, flash
from model import Model, label_count, allowed_image
from configs import Config


app = Flask(__name__)
app.config.from_object(Config)
model = Model()


@app.route('/', methods=['GET', 'POST'])
def upload_predict():

    if request.method == 'POST':
        image_file = request.files['image']

        if image_file:

            if allowed_image(image_file.filename):
                flash('Image uploaded successfully', category='success')
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename))
                img = cv2.imread(fr'static\files\{image_file.filename}')
                results = model.predict(image_file.filename)
                labels = label_count(results)

                return render_template('index.html',
                                        image_loc=image_file.filename,
                                        width=min(img.shape[1], 600),
                                        height=min(img.shape[0], 400),
                                        labels=labels)

            else:
                flash('Valid extensions: png, jpg, jpeg', category='error')
                return render_template('index.html', image_loc=None)

    return render_template('index.html', image_loc=None)



if __name__ == '__main__':
    app.run()