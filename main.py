from src.image_processor import ImageProcessor

if __name__ == "__main__":
    img_path = "input_images"
    img_target_size = 640
    processor = ImageProcessor(img_path)
    processor.process_folder(img_target_size)

    print("Folder successfully processed")
