# 🧠 AI Pokédex

This is an AI-powered Pokédex web app that identifies any of the original 151 Pokémon from a sprite or anime screenshot and displays detailed information such as type, ability, base stats (BST), and Pokédex entry — along with front/back/shiny sprites.

## 🚀 Features

- 🔍 Identify Gen 1 Pokémon using AI from any sprite (Gen 1–5) or anime screenshot
- 📸 Supports front, back, shiny, and non-shiny sprites
- 🧠 Image classification powered by PyTorch & ResNet
- 🌐 Flask-based web app interface
- 📊 Shows Pokémon types, abilities, BST, and original Pokédex description

## 🖼 Example

Upload an image like:

/dataset/pikachu/front/pikachu.png

makefile
Copy
Edit

Output:

Name: Pikachu
Type: Electric
Ability: Static
BST: 320
Description: When several of these Pokémon gather, their electricity could build and cause lightning storms.

markdown
Copy
Edit

## 🧠 Model

- Model: ResNet-18
- Framework: PyTorch
- Trained on: Gen 1 Pokémon sprites from Generations 1–5 (front/back, shiny/non-shiny) + anime screenshots
- Input size: 96x96
- Loss: CrossEntropy
- Optimizer: Adam

## 📁 Project Structure

ai-pokedex/
├── app.py # Flask app for image upload & display
├── model.py # Model loading and prediction logic
├── train.py # Model training script
├── dataset/ # Training images (sprites & anime)
├── templates/
│ └── index.html # Web interface
├── static/
│ └── uploaded/ # Uploaded images
├── gen1_pokemon_metadata.csv # Pokémon metadata
└── README.md

perl
Copy
Edit

## ⚙️ Requirements

```bash
pip install torch torchvision flask pandas pillow
▶️ Run the App
bash
Copy
Edit
python3 app.py
Then open your browser at:
👉 http://localhost:5000

📦 Training the Model (Optional)
If you want to retrain:

bash
Copy
Edit
python3 train.py
Model will be saved as sprite_classifier.pt.

📜 License
MIT License

Created with ❤️ using OpenAI and Jetson Orin Nano

