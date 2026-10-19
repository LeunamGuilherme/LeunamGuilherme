import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path, output_path="source-prepped.png"):
    print("A remover o fundo e a tratar a imagem...")
    inp = Image.open(input_path)
    out = remove(inp)
    
    img_np = np.array(out)
    
    if img_np.shape[2] == 4:
        r, g, b, a = cv2.split(img_np)
        rgb = cv2.merge([r, g, b])
    else:
        rgb = img_np
        a = np.ones(rgb.shape[:2], dtype=np.uint8) * 255

    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    white_bg = np.full_like(enhanced, 255)
    final_img = np.where(a > 0, enhanced, white_bg)

    cv2.imwrite(output_path, final_img)
    print(f"Foto tratada salva em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/prep_photo.py NOME_DA_IMAGEM")
    else:
        prep_photo(sys.argv[1])
