from flask import Flask , render_template,send_file,redirect,request
from rembg import remove
import tempfile 
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/remove_bg", methods=['POST'])

def background_remove():
    file= request.files['image'] 
    image_data = file.read()
    
    try:
        bg_removed = remove(image_data)
        temp_image = tempfile.NamedTemporaryFile(delete= False ,suffix=".png")
        temp_image.write(bg_removed)
        temp_image.close()
        return send_file(temp_image.name,as_attachment=True)
    except Exception as e:
        return str(e)
    

if __name__ =="__main__":
    app.run(debug=True)