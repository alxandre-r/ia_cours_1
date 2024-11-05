import os
from datetime import datetime
from PIL import Image, ImageOps


class ImageProcessor:

    def __init__(self, path: str):
        self._path = path

    def process_folder(self, img_target_size: int):
        output_id = datetime.now().strftime("%Y%m%d%H%M%S")
        output_folder = f"datasets/{output_id}"

        try:
            os.makedirs(output_folder, exist_ok=True)
        except OSError as e:
            print(f"Error while creating folder : {e}")

        for name_file in os.listdir(self._path):
            img_path = os.path.join(self._path, name_file)
            if os.path.isfile(img_path):
                self.process_img(img_path, output_folder, img_target_size)

    def process_img(self, img_path: str, output_folder: str, img_target_size: int):
        img = Image.open(img_path)
        try:
            ratio = img.width / img.height

            if ratio > 1:
                # Image is wider than tall: add padding at the bottom
                new_width = img_target_size
                new_height = int(img_target_size / ratio)
                resized_img = img.resize((new_width, new_height))
                vertical_padding = img_target_size - new_height
                fill_color = (0, 0, 0) if img.mode == "RGB" else 0
                padded_img = ImageOps.expand(
                    resized_img,
                    border=(0, 0, 0, vertical_padding),
                    fill=fill_color,
                )

            elif ratio < 1:
                # Image is taller than wide: add padding on the right
                new_height = img_target_size
                new_width = int(img_target_size * ratio)
                resized_img = img.resize((new_width, new_height))
                padding_horizontal = img_target_size - new_width
                fill_color = (0, 0, 0) if img.mode == "RGB" else 0
                padded_img = ImageOps.expand(
                    resized_img,
                    border=(0, 0, padding_horizontal, 0),
                    fill=fill_color,
                )

            else:
                # Image is square
                padded_img = img.resize((img_target_size, img_target_size))

            output_path = os.path.join(output_folder, os.path.basename(img_path))
            padded_img.save(output_path)

        finally:
            img.close()
