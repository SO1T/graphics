from PIL import Image
from scipy import ndimage


def min_max_median_filter(path, size=5):
    img = Image.open(path)
    for filter_type in ("minimum", "maximum", "median"):
        new_img = getattr(ndimage.filters, f"{filter_type}_filter")(img, size)
        new_path = path.rsplit(".", 1)[0] + f"_{filter_type}{size}_filtered.png"
        Image.fromarray(new_img).save(new_path)


path = "img/car.png"
min_max_median_filter(path)
min_max_median_filter(path, size=3)