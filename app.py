#!/usr/bin/python

import cv2 as cv
from utils import yolo, GrabCut
import numpy as np
import streamlit as st


def run():
    yolopath = "./truchav4"
    confidence = 0.25
    threshold = 0.45

    st.title("Truchav4 demo")

    uploaded_img = st.file_uploader("Choose an image...", type=['png', 'jpg', 'bmp', 'jpeg'])
    if uploaded_img is not None:
        file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
        image = cv.imdecode(file_bytes, 1)

        st.write("This is your uploaded image:")
        st.image(image, caption='Uploaded Image', channels="BGR", use_column_width=True)

        boxes, idxs = yolo.runYOLOBoundingBoxes_streamlit(image, yolopath, confidence, threshold)
        result_images = GrabCut.runGrabCut(image, boxes, idxs)

        st.write("")
        st.write("finish grabcut")
        st.write(f"There are {len(result_images)} segmented fish image. Each listed as below:")
        for i in range(len(result_images)):
            #cv.imwrite(f'grabcut{i}.jpg', result_images[i])
            st.image(result_images[i], channels="BGR", use_column_width=True)

if __name__ == '__main__':
    run()
