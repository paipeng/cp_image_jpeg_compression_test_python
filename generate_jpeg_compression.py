
from PIL import Image
import os
import argparse





def parse_arg():
    parser = argparse.ArgumentParser(description="A test script to generate image in different jpeg compression")
    parser.add_argument("inputImage", help="Input image")
    parser.add_argument("-o", "--outputPath", default="./", help="Output file path")
    args = parser.parse_args()
    print(f"Input file: {args.inputImage}")
    print(f"Output file: {args.outputPath}")
    return args






if __name__ == "__main__":
    args = parse_arg()
    
    if not os.path.exists(args.outputPath):
        os.makedirs(args.outputPath)

    try:
        image = Image.open(args.inputImage)
        print("Image loaded successfully!")
    except IOError as e:
        print(f"Error loading image: File '{args.inputImage}' not found or cannot be read. {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)