import torch
import torchvision.transforms as T
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor

# Load the pre-trained Detectron2 model
model_path = "model_weights.pth"  # Path to the pre-trained model weights
cfg = get_cfg()
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
cfg.merge_from_file("C:\Users\SAHANA\Desktop\plastic\model.yaml")  # Path to the model configuration file
cfg.MODEL.WEIGHTS = model_path
predictor = DefaultPredictor(cfg)

# Load and preprocess the image
image_path = "path_to_your_image.jpg"  # Path to your input image
image = T.ToTensor()(Image.open(image_path))

# Perform object detection
outputs = predictor(image)

# Access the predicted bounding boxes, labels, and scores
predicted_boxes = outputs["instances"].pred_boxes.tensor
predicted_labels = outputs["instances"].pred_classes
predicted_scores = outputs["instances"].scores

# Print the detected objects and their confidence scores
for box, label, score in zip(predicted_boxes, predicted_labels, predicted_scores):
    print(f"Label: {label}, Score: {score.item()}")

