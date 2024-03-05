#!/usr/local/bin/python3

import glob
import json
import numpy as np
from PIL import Image as PILImage
import cv2
import matplotlib.pyplot as plt
import inspect
import netCDF4


def list_files():
    with open("/etc/ftp_gsmap.settings.json") as f:
        settings_text = f.read()
        settings = json.loads(settings_text)
        root_path = settings["root_path"]
        file_types = settings["file_types"]

        files = glob.glob(root_path + file_types)
        return files


def load_from_nc4(file):
    nc = netCDF4.Dataset(file, "r")
    nc_src = nc.variables["Tb"][0].data.astype("uint16")
    nc_mask = nc.variables["Tb"][0].mask.astype("uint8")
    return nc_src, nc_mask


def save_as_png(image, file):
    nc_img = PILImage.fromarray(image, "L")
    nc_img.save(file)


def main():
    file = "../results/merg_2023010100_4km-pixel.nc4"
    nc_src, nc_mask = load_from_nc4(file)
    nc_src = cv2.resize(nc_src, None, fx=0.4, fy=0.4)
    nc_mask = cv2.resize(nc_mask, nc_src.shape[::-1])

    nc_inpainted = cv2.inpaint(nc_src, nc_mask, 3, cv2.INPAINT_TELEA)

    save_as_png(nc_src, "result.ong")
    save_as_png(nc_inpainted, "result_inpainted.ong")


if __name__ == "__main__":
    main()
