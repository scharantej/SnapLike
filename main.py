
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Create a Flask app
app = Flask(__name__)

# Set up the database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define the Photo model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    image_filename = db.Column(db.String(120))
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Photo {self.id}: {self.title}>"

# Create the database tables
db.create_all()

# Define the home route
@app.route('/')
def home():
    # Get all the photos from the database
    photos = Photo.query.all()
    # Render the home page with the photos
    return render_template('index.html', photos=photos)

# Define the photo detail route
@app.route('/photo/<int:photo_id>')
def photo_detail(photo_id):
    # Get the photo with the specified ID from the database
    photo = Photo.query.get_or_404(photo_id)
    # Render the photo detail page with the photo
    return render_template('photo-detail.html', photo=photo)

# Define the upload photo route
@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    # Get the form data
    title = request.form['title']
    description = request.form['description']
    image = request.files['image']
    # Save the image to the uploads folder
    filename = secure_filename(image.filename)
    image.save(os.path.join('uploads', filename))
    # Create a new photo object and save it to the database
    photo = Photo(title=title, description=description, image_filename=filename)
    db.session.add(photo)
    db.session.commit()
    # Redirect to the home page
    return redirect(url_for('home'))

# Define the like photo route
@app.route('/like-photo', methods=['POST'])
def like_photo():
    # Get the photo ID from the form data
    photo_id = request.form['photo_id']
    # Get the photo with the specified ID from the database
    photo = Photo.query.get_or_404(photo_id)
    # Increment the photo's like count and save the changes to the database
    photo.likes += 1
    db.session.commit()
    # Redirect to the photo detail page
    return redirect(url_for('photo_detail', photo_id=photo_id))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
