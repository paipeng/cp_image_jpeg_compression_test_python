
from PIL import Image, ImageFilter
import os
import argparse





def parseArg():
    parser = argparse.ArgumentParser(description="A test script to generate image in blur filter")
    parser.add_argument("inputImage", help="Input image")
    parser.add_argument("-b", "--blur", default="1", help="blur filter sizes, format: 10-5-100 % (from min 10 to max 100 with step 5 ); 100 (from min 100 to max 100 wit step 1)")
    parser.add_argument("-o", "--outputPath", default="./", help="Output file path")
    args = parser.parse_args()
    print(f"Input file: {args.inputImage}")
    print(f"blur: {args.blur}")
    print(f"Output file: {args.outputPath}")
    return args

def imageSaveBmp(image: Image, size: int, filename: str):
    bmpFilename = filename + '_' + f'{size:0>3}' + '.bmp'
    image.save(bmpFilename)


def parseSizes(size: str):
    minSize = 100
    maxSize = 100
    step = 1

    s = size.split('-')
    print(len(s))
    print(s[0])
    if len(s) == 3:
        minSize = int(s[0])
        step = int(s[1])
        maxSize = int(s[2])
    elif len(s) == 2:
        minSize = int(s[0])
        maxSize = int(s[1])
    elif len(s) == 1:
        minSize = int(s[0])
        maxSize = int(s[0])
    print(f'minSize {minSize} step: {step} maxSize: {maxSize}')
    return [minSize, step, maxSize]

def parserFilename(filename: str) -> str:    
    last_slash_index = filename.rfind(os.path.sep)
    if last_slash_index > 0:
        filename = filename[last_slash_index+1:]
    else:
        filename = filename
    print(filename)

    # remove file extension
    last_dot_index = filename.rfind(".")
    jpegFilename = filename[:last_dot_index]

    return jpegFilename


if __name__ == "__main__":
    args = parseArg()
    
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)

    try:
        image = Image.open(args.inputImage)
        print("Image loaded successfully!")


        blurs = parseSizes(args.blur)
        print(blurs)

        filename = parserFilename(args.inputImage)
        print(filename)

        for index in range(blurs[0], blurs[2] + 1, blurs[1]):
            print(f'index: {index}')
            blurred_image = image.filter(ImageFilter.GaussianBlur(radius=index))
            imageSaveBmp(image=blurred_image, size=index, filename=args.outputPath + os.path.sep + filename)


    except IOError as e:
        print(f"Error loading image: File '{args.inputImage}' not found or cannot be read. {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)