# Image_To_Pixel_Conversion
Converting images into a representation of their constituent pixels.

The implementation of a Python script designed to convert an input image into its constituent pixel values, extract color names using RGB values, and visualize RGB histograms. 
The script utilizes various libraries such as OpenCV, NumPy, Matplotlib, and Webcolors for image processing, data manipulation, visualization, and color recognition.

Implementation Details:

1. Image Processing and Pixel Extraction
Functionality: The script reads an input image (image.jpg), converts it from BGR to RGB format using OpenCV, and extracts pixel values.

Methodology:

OpenCV: Used to read and manipulate the image.
NumPy: Utilized for efficient array operations to store pixel values.
Pixel Representation: Pixel values are stored in both list and NumPy array formats.
                      Each pixel is represented by its RGB components (Red, Green, Blue).

2. Color Name Extraction
Functionality: Determines color names corresponding to RGB values extracted from the image pixels.

Methodology:

Webcolors Library: Converts RGB values to hex format and retrieves color names for each pixel values.
Closest Color Matching: If an exact match isn't found, the script identifies the closest color name based on RGB proximity.

3. Visualization
Functionality: Visualizes histograms for the Red, Green, and Blue channels of the image pixels.

Methodology:

Matplotlib: Used to create histograms for both list and NumPy array representations of pixel values.

4. Output
5. 
The script will print the total number of pixels and example pixel values.
It will save the pixel values and their corresponding color names to pixel_info.txt.
Histograms of the RGB channels will be displayed.
