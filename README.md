## Flask Photo Sharing App Design

### HTML Files

1. **index.html**: This will be the main HTML file that serves as the homepage of the app. It will display a gallery of photos and a form for uploading new photos.
2. **photo-detail.html**: This HTML file will display a detailed view of a single photo. It will include information such as the photo's title, description, and the option to like the photo.

### Routes

1. **@app.route('/'):** This is the *home* route. It will handle requests to the root URL of the application and will render the **index.html** file.
2. **@app.route('/photo/<int:photo_id>'):** This route will handle requests to a specific photo's details. It will render the **photo-detail.html** file and pass the corresponding photo's data to the template.
3. **@app.route('/upload-photo', methods=['POST']):** This route will handle requests to upload new photos to the application. It will receive form data containing the photo's title, description, and the image file itself, and will save the photo to the database.
4. **@app.route('/like-photo', methods=['POST']):** This route will handle requests to like a photo. It will receive form data containing the ID of the photo being liked and update the database to reflect the like.