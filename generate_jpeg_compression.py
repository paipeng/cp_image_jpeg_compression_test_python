
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
    jpegFilename = filename + '_' + f'{compression:0>3}' + '.jpeg'
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


        compression = parseCompression(args.compression)
        print(compression)

        filename = parserFilename(args.inputImage)
        print(filename)

        for index in range(compression[0], compression[2] + 1, compression[1]):
            print(f'index: {index}')
            imageJpegCompression(image=image, compression=index, filename=args.outputPath + os.path.sep + filename)


    except IOError as e:
        print(f"Error loading image: File '{args.inputImage}' not found or cannot be read. {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)