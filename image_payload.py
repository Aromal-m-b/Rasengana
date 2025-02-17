import cv2
import numpy as np, matplotlib.pyplot as plt, random
import base64, json

def image_to_payload(image_path):
    # Read the image using OpenCV
    orig_image = cv2.imread(image_path)

# Calculate the parameters for image resizing
    image_height, image_width, _ = orig_image.shape
    model_height, model_width = 640, 640
    x_ratio = image_width/model_width
    y_ratio = image_height/model_height

# Resize the image as numpy array
    resized_image = cv2.resize(orig_image, (model_height, model_width))
# Conver the array into jpeg
    resized_jpeg = cv2.imencode('.jpg', resized_image)[1]
# Serialize the jpg using base 64
    payload = base64.b64encode(resized_jpeg).decode('utf-8')

    payload = base64.b64encode(resized_jpeg).decode('utf-8')
    
    return payload

def save_payload_to_file(payload, file_path):
    # Write the base64 payload to a text file
    with open(file_path, "w") as file:
        file.write(payload)
    print(f"Payload saved to {file_path}")

# Example usage
image_path = "C:/Users/USER/Downloads/W.jpg"  # Path to your image file
payload = image_to_payload(image_path)
file_path = 'c:/Users/USER/Downloads/image_payload.txt'  # Path to the text file where the payload will be saved
save_payload_to_file(payload, file_path)
