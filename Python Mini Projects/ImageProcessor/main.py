from PIL import Image, ImageEnhance, ImageFilter
import os



def main():
    print("Hello from imageprocessor!")
    path= './imgs'
    path_out= './edited_imgs'

    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-90, expand=True)



        factor = 1.5
        enhance = ImageEnhance.Contrast(edit)
        edit = enhance.enhance(factor)

        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{path_out}/{clean_name}_edited.jpg")

    print("All done!")



if __name__ == "__main__":
    main()
