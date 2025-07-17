from flask import Flask, request, render_template
from pokedex import get_pokemon_info
from model import classify_sprite
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        image = request.files.get("sprite_image")
        if image:
            image_path = os.path.join(UPLOAD_FOLDER, "input.png")
            image.save(image_path)

            predicted_name = classify_sprite(image_path)
            result = get_pokemon_info(predicted_name)

         
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
