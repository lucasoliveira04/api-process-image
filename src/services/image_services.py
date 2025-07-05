from model.image_model import ImageModel
from pathlib import Path
from uuid import uuid4
from PIL import Image

def get_image_folder():
    images_dir = Path("C:/Imagens_Redimensionadas")
    images_dir.mkdir(parents=True, exist_ok=True)
    return images_dir


def image_services(file, image_width: int, image_height: int):
    try:
        images_dir = get_image_folder()
        images_width = int(image_width)
        images_height = int(image_height)

        new_filename = f"{uuid4().hex}_{file.filename}"
        image_path = images_dir / new_filename

        file.save(str(image_path))

        img = Image.open(image_path)
        resized_image = img.resize((images_width, images_height))
        resized_image.save(image_path)

        image = ImageModel(
            imageId=uuid4().hex,
            imageName=new_filename,
            imageWidth=resized_image.width,
            imageHeight=resized_image.height,
            imageType=img.format,
            imagePath=str(image_path),
            imagePathFinal=str(image_path),
            imageStatus="processed"
        )

        return image.to_dict()
    except Exception as e:
        print(f"Error processing image: {e}")
        return {"error": str(e)}