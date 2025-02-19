#POST request format
#{
#  "body": "{\"key1\": \"value1\"}"
#}
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

def invoke(image_details):
    url = "https://psilvhbvp5.execute-api.us-east-1.amazonaws.com/endpoint/dev"

# Create the inner JSON data
    inner_data = {
        "image_data": image_to_payload(image_details)
    }
# Create the payload where "body" is a JSON-string of the inner data
    payload = {
        "body": json.dumps(inner_data)
    }

# Convert the entire payload to a JSON string
    payload_json = json.dumps(payload)

# Define the headers
    headers = {
        "Content-Type": "application/json"
    }

# Send the POST request
    response = requests.post(url, headers=headers, data=payload_json)

# Print the response
    #print("Status Code:", response.status_code)
    data = response.json()
    
    #print("Response Body:", data["body"])
    return data["body"]

print(invoke("C:/Users/USER/Downloads/W.jpg"))

