from PIL import Image

original_image_path = "../../datasets/20240824_154535.jpg"
updated_image_pah = "datasets/outputTest_img.jpg"

original_image = Image.open(original_image_path)

# resized_image = image.resize((300, 300))

rotated_image = original_image.rotate(-90)
rotated_image.save(updated_image_pah)

print("Image", original_image_path, "has been updated and saved to", updated_image_pah)
