
from PIL import Image
import os
import argparse





def parseArg():
    parser = argparse.ArgumentParser(description="A test script to generate image in different jpeg compression")
    parser.add_argument("inputImage", help="Input image")
    parser.add_argument("-c", "--compression", default="100", help="JPEG compression, format: 10-5-100 (from min 10 to max 100 with step 5); 100 (from min 100 to max 100 wit step 1)")
    parser.add_argument("-o", "--outputPath", default="./", help="Output file path")
    args = parser.parse_args()
    print(f"Input file: {args.inputImage}")
    print(f"compression: {args.compression}")
    print(f"Output file: {args.outputPath}")
    return args

def imageJpegCompression(image: Image, compression: int, filename: str):
    # remove file extension
    last_dot_index = filename.rfind(".")
    jpegFilename = filename[:last_dot_index]
    jpegFilename = jpegFilename + '_' + f'{compression:0>3}' + '.jpeg'
    image.save(jpegFilename, quality=compression, optimize = True)

def parseCompression(compression: str):
    minCompression = 100
    maxCompression = 100
    step = 1

    s = compression.split('-')
    print(len(s))
    print(s[0])
    if len(s) == 3:
        minCompression = int(s[0])
        step = int(s[1])
        maxCompression = int(s[2])
    elif len(s) == 2:
        minCompression = int(s[0])
        maxCompression = int(s[1])
    elif len(s) == 1:
        minCompression = int(s[0])
        maxCompression = int(s[0])
    print(f'minCompression {minCompression} step: {step} maxCompression: {maxCompression}')
    return [minCompression, step, maxCompression]

if __name__ == "__main__":
    args = parseArg()
    
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)

    try:
        image = Image.open(args.inputImage)
        print("Image loaded successfully!")


        compression = parseCompression(args.compression)
        print(compression)


        for index in range(compression[0], compression[1], compression[2]):
            printf('index: {index}')

    except IOError as e:
        print(f"Error loading image: File '{args.inputImage}' not found or cannot be read. {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)