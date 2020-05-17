import numpy as np
from PIL import Image


def setCharByLSB(color, char):
    binaryColor = np.binary_repr(color, width=8)
    binaryChar = format(ord(char), '08b')
    binaryColor = binaryColor[:7] + binaryChar[7]
    return int(binaryColor, 2)


class LSB:

    def encode(self, path, message, outputFileName):
        image = Image.open(path)
        binnaryMessage = format(ord(message), '08b')
        lenOfBinnaryMessage = len(binnaryMessage)
        width, height = image.size
        index = 0

        for row in range(height):
            for col in range(width):
                pixel = image.getpixel((col, row))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]

                if(lenOfBinnaryMessage > index):
                    r = setCharByLSB(r, binnaryMessage[index])
                    print(binnaryMessage[index])
                if(lenOfBinnaryMessage > index + 1):
                    g = setCharByLSB(g, binnaryMessage[index + 1])
                    print(binnaryMessage[index + 1])
                if(lenOfBinnaryMessage > index + 2):
                    b = setCharByLSB(b, binnaryMessage[index + 2])
                    print(binnaryMessage[index + 2])

                index += 3

        image.save(outputFileName)

    def decode(self, path):
        image = Image.open(path)
        width, height = image.size
        bitab = []

        for row in range(height):
            for col in range(width):
                pixel = image.getpixel((col, row))
                for color in pixel:
                    x = np.binary_repr(color, width=8)
                    bitab.append(x[7]) if len(bitab) < 8 else False
