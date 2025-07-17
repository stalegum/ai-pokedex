import torch
from torchvision import transforms, models
from PIL import Image
import os

# Get list of Pokémon names from dataset folders
class_names = sorted(os.listdir("dataset"))

# Load model
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load("sprite_classifier.pt", map_location="cpu"))
model.eval()

def classify_sprite(image_path):
    transform = transforms.Compose([
        transforms.Resize((96, 96)),
        transforms.ToTensor()
    ])
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        pred_idx = output.argmax(1).item()
        return class_names[pred_idx]
