#Image to Pixel Conversion into List as well as Numpy Array

import cv2
import numpy as np
import matplotlib.pyplot as plt
import webcolors

# Function to convert image to pixel
def image_to_pixels(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get image shape
    height, width, _ = image_rgb.shape

    # Initialize empty list for pixel values
    pixel_values_list = []

    # Initialize empty NumPy array for pixel values
    pixel_values_np = np.zeros((height * width, 3), dtype=np.uint8)

    # Iterate through each pixel and extract RGB values
    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = image_rgb[y, x]
            pixel_values_list.append((r, g, b))
            pixel_values_np[index] = [r, g, b]
            index += 1

    return pixel_values_list, pixel_values_np

#Function to get the closest colour according to RGB VALUE
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

#Function to get the color name
def get_color_name(rgb_tuple):
    try:
        # Convert RGB to hex
        hex_value = webcolors.rgb_to_hex(rgb_tuple)
        # Get the color name directly
        return webcolors.hex_to_name(hex_value)
    except ValueError:
        # If exact match not found, find the closest color
        return closest_color(rgb_tuple)


# Function to write pixel values and correspoing color name to a file
def write_pixel_values_to_file(pixel_values, color_names, file_path):
    with open(file_path, 'w') as f:
        for i, pixel in enumerate(pixel_values):
            r, g, b = pixel
            color_name = color_names[i]
            f.write(f"Pixel {i+1}: RGB({r}, {g}, {b}) -> Color Name: {color_name}\n")

# Function to plot histograms of RGB values
def plot_rgb_histograms(pixel_values_list, pixel_values_np):
    r_vals_list = [pixel[0] for pixel in pixel_values_list]
    g_vals_list = [pixel[1] for pixel in pixel_values_list]
    b_vals_list = [pixel[2] for pixel in pixel_values_list]

    r_vals_np = pixel_values_np[:, 0]
    g_vals_np = pixel_values_np[:, 1]
    b_vals_np = pixel_values_np[:, 2]

    plt.figure(figsize=(12, 6))

    # Plot histograms for pixel values in list format
    plt.subplot(2, 3, 1)
    plt.hist(r_vals_list, bins=256, color='red', alpha=0.5)
    plt.title('Red Channel (As_List)')

    plt.subplot(2, 3, 2)
    plt.hist(g_vals_list, bins=256, color='green', alpha=0.5)
    plt.title('Green Channel (As_List)')

    plt.subplot(2, 3, 3)
    plt.hist(b_vals_list, bins=256, color='blue', alpha=0.5)
    plt.title('Blue Channel (As_List)')

    # Plot histograms for pixel values in NumPy array format
    plt.subplot(2, 3, 4)
    plt.hist(r_vals_np, bins=256, color='red', alpha=0.5)
    plt.title('Red Channel (NumPy Array)')

    plt.subplot(2, 3, 5)
    plt.hist(g_vals_np, bins=256, color='green', alpha=0.5)
    plt.title('Green Channel (NumPy Array)')

    plt.subplot(2, 3, 6)
    plt.hist(b_vals_np, bins=256, color='blue', alpha=0.5)
    plt.title('Blue Channel (NumPy Array)')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    # Path to image file
    image_path = 'image.jpg'

    # Convert image to pixel representation
    pixels_list, pixels_np = image_to_pixels(image_path)

    # Output pixel information
    print(f"Total pixels: {len(pixels_list)}")
    print("Example pixels (RGB values):", pixels_list[:10])  # Print first 10 pixels as example

    # Finding color names for each pixel
    color_names = []
    for pixel in pixels_list:
        color_name = get_color_name(pixel)
        color_names.append(color_name)

    # Converting pixel list to NumPy array for comparison
    pixels_np_from_list = np.array(pixels_list)

    # Verifying both arrays are identical or not
    print("Arrays are identical:", np.array_equal(pixels_np, pixels_np_from_list))

    # Write pixel values and color names to files
    pixel_info_file_path = 'pixel_info1.txt'
    write_pixel_values_to_file(pixels_list, color_names, pixel_info_file_path)

    print(f"Pixel values and color names written to '{pixel_info_file_path}'")

    # Plot histograms of RGB values
    plot_rgb_histograms(pixels_list, pixels_np)
    num_pixels_to_print = 50
    print(f"\nColor names for the first {num_pixels_to_print} pixels:")
    for i in range(num_pixels_to_print):
        rgb_tuple = pixels_list[i]
        color_name = get_color_name(rgb_tuple)
        print(f"Pixel {i + 1}: RGB {rgb_tuple} -> Color Name: {color_name}")