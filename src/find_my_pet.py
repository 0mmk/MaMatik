import streamlit as st
import cv2
import os
import emoji


def main():


    st.title(emoji.emojize('The Ultimate MaMatik :dog:'))
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    # user uploads their pets photos, could be one or more photos
    uploaded_image = st.file_uploader('Sahibi olduğunuz hayvanın bir veye birden çok fotoğrafını yüyleyiniz. ',accept_multiple_files=1)
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
        current_image = './data/capture' + str(st.session_state.capture) + '.jpg'


    # output >> signal


    # if signal
    #   trigger user
    if st.button('test'):
        cv2.destroyAllWindows()
        cv2.imshow('Final', current_image)

if __name__ == "__main__":
    main()