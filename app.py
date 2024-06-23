from flask import Flask, render_template,send_file
import base64
import os
from PIL import Image
from io import BytesIO


app = Flask(__name__)
# Define the path to your HTML file
def image_upper(image_path):
    image = Image.open(image_path)
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def other_images(image_path):
    new_width = 720 # Adjust the new width as needed
    new_height = 550  # Adjust the new height as needed
    image = Image.open(image_path)
    # Resize the image with the new dimensions while maintaining the aspect ratio
    resized_image = image.resize((new_width, new_height))
    
    buffered = BytesIO()
    resized_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return img_str

    

@app.route('/')
def home():
    # Get the absolute path to the HTML file

     # Path to your image
    image_str_path = "static/my_image.jpg"
    img_str=image_upper(image_str_path)







    kerela_path = "static/k2.jpg"
    mine="static/1.jpg"


    recent_image1=other_images(mine)
    k2_image2=other_images(kerela_path)

    # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()



    return render_template('new_index.html', img_str=img_str,recent_image1=recent_image1,k2=k2_image2)

@app.route('/myendeavors')
def myendeavors():


     # Path to your image
    image_path = "static/my_image.jpg"
    img_str=image_upper(image_path)

    # # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('new_myendeavors.html', img_str=img_str)




@app.route('/nowpage')
def nowpage():


    image_path = "static/my_image.jpg"
    img_str=image_upper(image_path)
    # # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('new_nowpage.html', img_str=img_str)



@app.route('/thoughts')
def thoughts():


    image_path = "static/my_image.jpg"
    img_str=image_upper(image_path)
    # # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('new_thoughts.html', img_str=img_str)



@app.route('/projects')
def projects():


    image_path = "static/my_image.jpg"
    img_str=image_upper(image_path)

    # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('new_projects.html', img_str=img_str)


@app.route('/articles')
def articles():


    image_path = "static/my_image.jpg"
    img_str=image_upper(image_path)

    # # Open and convert the image to base64
    # image = Image.open(image_path)
    # buffered = BytesIO()
    # image.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('new_articles.html', img_str=img_str)



if __name__ == '__main__':
    app.run(debug=True)