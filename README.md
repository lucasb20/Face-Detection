# ImageToTextConverter

## Overview
ImageToTextConverter is a simple C++ application that converts images to text. It takes an image file as input and generates a corresponding text representation of the image.

## Features
- Converts images to text
- Supports various image formats (e.g., PNG, JPEG, BMP)
- Customizable output options

## Installation
To build and use ImageToTextConverter, follow these steps:
1. Clone the repository: `git clone https://github.com/lucasb20/ImageToTextConverter.git`
2. Navigate to the project directory: `cd ImageToTextConverter`
3. Compile the source code: `g++ -o ImageToTextConverter main.cpp ImageConverter.cpp`
4. Run the application: `./ImageToTextConverter`

## Usage
To convert an image to text, run the application and provide the path to the image file as a command-line argument. For example:

```bash
./ImageToTextConverter path/to/image.png
```

By default, the text output will be printed to the console. You can customize the output by modifying the source code or using command-line options (if available).

## Screenshots