import picamera, json, requests, os, random
from time import sleep
from PIL import Image, ImageDraw

#capture an image
camera = picamera.PiCamera()
camera.capture('image1.jpg')
print('caputred image')

#make a prediction on the image
url = 'https://app.nanonets.com/api/v2/ObjectDetection/LabelFile/'
data = {'file': open('image1.jpg', 'rb'), \
    'modelId': ('', 'YOUR_MODEL_ID')}
response = requests.post(url, auth=requests.auth.HTTPBasicAuth('YOUR_API_KEY', ''), files=data)
print(response.text)

#draw boxes on the image
response = json.loads(response.text)
im = Image.open("image1.jpg")
draw = ImageDraw.Draw(im, mode="RGBA")
prediction = response["result"][0]["prediction"]
for i in prediction:
    draw.rectangle((i["xmin"],i["ymin"], i["xmax"],i["ymax"]), fill=(random.randint(1, 255),random.randint(1, 255),random.randint(1, 255),127))
im.save("image2.jpg")
os.system("xdg-open image2.jpg")