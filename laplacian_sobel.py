from PIL import Image
import cv2

def laplacian(path, ddepth=-1, ksize=1):
    img = cv2.imread(path)
    new_img = cv2.Laplacian(img, ddepth, ksize=ksize)
    new_path = path.rsplit(".", 1)[0] + f"_laplacian{ksize}_filtered.png"
    Image.fromarray(new_img).save(new_path)


def sobel(path, ddepth=-1, ksize=3):
    img = cv2.imread(path)
    for i, direction in enumerate(("x", "y")):
        new_img = cv2.Sobel(img, ddepth, 1 - i, i, ksize=ksize)
        new_path = path.rsplit(".", 1)[0] + f"_sobel{ksize}_{direction}_filtered.png"
        Image.fromarray(new_img).save(new_path)


path = "img/car.png"
laplacian(path)
laplacian(path, ksize=3)
laplacian(path, ksize=5)

sobel(path)
sobel(path, ksize=5)