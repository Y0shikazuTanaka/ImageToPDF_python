import os
import re
import img2pdf
from PIL import Image
import config


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


class PdfCreater:
    def __init__(self):
        c = config.Config()
        self.chekImgFormatList = c.imgFormats.split(',')

    def createPDF(self, dir_path, out_pdf_path):
        self.convertPngToJpeg(dir_path)

        files = []
        for ext in self.chekImgFormatList:
            files.extend(dir_path.glob(f"*.{ext}"))

        if len(files) == 0:
            raise Exception(f"フォルダ内に画像ファイルがありません。{dir_path}")

        sort_files = sorted([str(f) for f in files], key=natural_keys)

        with open(f"{out_pdf_path}/{dir_path.name}.pdf", "wb") as f:
            f.write(img2pdf.convert([Image.open(f).filename for f in sort_files]))

    def convertPngToJpeg(self, dir_path):
        files = dir_path.glob(f"*.*")
        match = re.compile("(png)")
        for file_name in files:
            im = Image.open(file_name)
            im = im.convert("RGB")
            new_file_name = match.sub("jpeg", str(file_name))
            os.remove(file_name)
            im.save(new_file_name, quality=100)

