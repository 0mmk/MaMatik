import streamlit as st
import cv2
import os
import emoji
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
from PIL import Image, ImageOps

def main():
    
    st.title(emoji.emojize('Can Dostumu Bul'))
    st.write("MaMatikler bulundurduğu kamera sistemi sayesinde, mama yemek için gelen canlıların fotoğraflarını çeker ve kaydeder. Eğer sisteme kayıtı kayıp bir canlı eşleşmesi olursa MaMatik'in konumunu hayvan sahibine gönderilir.")

    # user uploads their pets photos, could be one or more photos
    uploaded_image = st.file_uploader('Sahibi olduğunuz hayvanın bir veye birden çok fotoğrafını yükleyiniz. ',accept_multiple_files=1)
    capture_image = st.button('Capture signal')


    # connects IP camera
    cap = cv2.VideoCapture("rtsp://admin:123456akdeniz@192.168.1.108:554/cam/realmonitor?channel=1@subtype=1")

    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

        # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame

    # when capture button is pressed system will take snapshot from IP camera and save under snaps folder
    if 'capture' not in st.session_state:
        st.session_state.capture = 0
    
    
    if capture_image:
        # reading from frame
        ret, frame = cap.read()

        
        if ret:
            name = './data/capture' + str(st.session_state.capture) + '.jpg'
            print('capture{}.jpg is saved ...'.format(st.session_state.capture))

            # writing the extracted images
            
            cv2.imwrite(name, frame)

            st.session_state.capture += 1

        cap.release()
        cv2.destroyAllWindows()


    # add model and take inpups from current_image
    if st.button('Predict'):
        current_photo = './data/capture' + str(st.session_state.capture - 1) + '.jpg'   
        predict(current_photo)
        display_map(41.089566, 29.095647)

def predict(predict_image):

    # Load the model
    model = load_model('keras_model.h5')


    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(predict_image)
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)

    print(prediction[0])

    dic = {}
    file = open("labels.txt").read()
    for line in file.splitlines():
        entry = line.split(" ")
        dic[int(entry[0])] = entry[1]
    
    prediction_answ = dic[np.argmax(prediction[0])]
    st.success(prediction_answ)
    st.image(predict_image)

def display_map(lat, lon):
    df = pd.DataFrame(
    np.array([[0, 0]]) + [lat, lon], columns=['lat', 'lon'])
    st.map(df)

if __name__ == "__main__":
    main()