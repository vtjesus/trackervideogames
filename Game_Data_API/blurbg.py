from PIL import Image, ImageFilter
import os


def process_image(
    image_path, output_path, scale_factor=0.1, blur_radius=10, quality=20
):
    """
    Process a single image: downscale, apply Gaussian blur, and save as JPEG.

    Parameters:
    - image_path: str - The path to the input image.
    - output_path: str - The path to save the processed image.
    - scale_factor: float - The downscale factor (e.g., 0.1 for 10% of the original size).
    - blur_radius: int - The radius for the Gaussian blur.
    - quality: int - The quality of the saved JPEG (1-100, where 100 is the best quality).
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size

            new_size = (int(width * scale_factor), int(height * scale_factor))
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)

            img_blurred = img_resized.filter(ImageFilter.GaussianBlur(blur_radius))

            output_filename = (
                os.path.basename(image_path).rsplit(".", 1)[0] + "_processed.jpg"
            )
            img_blurred.save(
                os.path.join(output_path, output_filename), "JPEG", quality=quality
            )
            print(f"Processed and saved: {output_filename}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")


def process_images_in_folder(
    input_folder, output_folder, scale_factor=0.1, blur_radius=10, quality=20
):
    """
    Process all images in the specified folder with the given parameters.

    Parameters:
    - input_folder: str - The path to the folder containing the images.
    - output_folder: str - The path to the folder where processed images will be saved.
    - scale_factor: float - The downscale factor.
    - blur_radius: int - The radius for the Gaussian blur.
    - quality: int - The quality of the saved JPEG.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            process_image(image_path, output_folder, scale_factor, blur_radius, quality)


process_images_in_folder('banner', 'output', 0.5, 50)

