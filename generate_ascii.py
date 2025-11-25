from PIL import Image, ImageOps
import sys

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.5
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_image

# ...



def pixels_to_ascii(image):
    # Ensure image is RGBA
    image = image.convert("RGBA")
    
    # Extract alpha channel
    alpha = image.split()[-1]
    
    # Find edges on alpha channel to get silhouette outline
    edges = alpha.filter(ImageFilter.FIND_EDGES)
    
    # Enhance edges
    enhancer = ImageEnhance.Contrast(edges)
    edges = enhancer.enhance(2.0)
    
    pixels = edges.getdata()
    
    chars = [" ", ".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
    
    ascii_str = ""
    for pixel in pixels:
        if pixel < 50: # Threshold for background
            ascii_str += " "
        else:
            # Map brightness to char index
            char_index = int(pixel / 255 * (len(chars) - 1))
            ascii_str += chars[char_index]
            
    return ascii_str

def main(image_path, output_path, new_width=60):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width=new_width)
    # No grayify needed, we handle RGBA in pixels_to_ascii
    
    ascii_chars = pixels_to_ascii(image)
    pixel_count = len(ascii_chars)
    ascii_image = "\n".join(ascii_chars[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    with open(output_path, "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    # Hardcoded paths for this task
    image_path = "/Users/jrudd/.gemini/antigravity/brain/1b20ce82-ab4b-4aac-9fb1-674907e5513f/uploaded_image_1764104837653.png"
    output_path = "funsize_engineer/assets/ascii-art.txt"
    main(image_path, output_path, new_width=80)

if __name__ == "__main__":
    # Hardcoded paths for this task
    image_path = "/Users/jrudd/.gemini/antigravity/brain/1b20ce82-ab4b-4aac-9fb1-674907e5513f/uploaded_image_1764105054574.png"
    output_path = "funsize_engineer/assets/ascii-art.txt"
    main(image_path, output_path, new_width=80)
