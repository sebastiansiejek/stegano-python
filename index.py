from PIL import Image
from LSB import LSB

# create image
image = Image.new(mode="RGB", size=(2, 2), color=(255, 0, 0))
image.save("image.png")

LSB().encode("image.png", "C", "image-secret.png")
LSB().decode("image-secret.png")
