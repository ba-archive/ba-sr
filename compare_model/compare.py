import os
from pathlib import Path
from PIL import Image
from icecream import ic

def sr_realcugan(source, output):
    status = os.popen(f"../vendors/realcugan/realcugan-ncnn-vulkan -s 4 -i {source} -o {output}").read()
    ic(status)

def sr_realsrgan(source, output):
    status = os.popen(f"../vendors/realesrgan/realesrgan-ncnn-vulkan -i {source} -o {output}").read()
    ic(status)

origin_img_path = Path("./momoka_spr.png")

origin_img = Image.open(origin_img_path)

width, height = origin_img.size

result_img = Image.new(origin_img.mode, (width * 3 * 4, height * 4))

sr_realcugan(origin_img_path, f"{origin_img_path.stem}-2x{origin_img_path.suffix}")
sr_realsrgan(origin_img_path, f"{origin_img_path.stem}-4x{origin_img_path.suffix}")
cugan_img = Image.open(f"{origin_img_path.stem}-2x{origin_img_path.suffix}")
srgan_img = Image.open(f"{origin_img_path.stem}-4x{origin_img_path.suffix}")

origin_img = origin_img.resize((width * 4, height * 4))
cugan_img = cugan_img.resize((width * 4, height * 4))
srgan_img = srgan_img.resize((width * 4, height * 4))

result_img.paste(origin_img)
result_img.paste(cugan_img, box=(width * 4, 0))
result_img.paste(srgan_img, box=(width * 2 * 4, 0))

result_img.show()
result_img.save("compare.png")