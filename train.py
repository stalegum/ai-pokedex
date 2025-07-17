import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import torch.nn as nn
import os

# Image transformations
transform = transforms.Compose([
    transforms.Resize((96, 96)),
    transforms.ToTensor()
])

# Load dataset
dataset = datasets.ImageFolder("dataset", transform=transform)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

# Build model
model = models.resnet18(weights=None)  # no pretrained weights
model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Training setup
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 🔁 Train for more epochs if accuracy is low
epochs = 50
print(f"🎯 Starting training for {epochs} epochs...")

for epoch in range(epochs):
    total_loss = 0
    model.train()
    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        loss = loss_fn(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"✅ Epoch {epoch+1}/{epochs} - Loss: {total_loss:.4f}")

# Save model
torch.save(model.state_dict(), "sprite_classifier.pt")
print("💾 Model saved as sprite_classifier.pt")
