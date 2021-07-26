import cv2
import pytesseract
import streamlit as st
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.title("Number Plate detection")
img = st.sidebar.file_uploader("Please upload a number plate")
if img is not None:
  img_read = Image.open(img)
  img_new = np.array(img_read)
if st.button('Detect Number Plate'):
  number_plate = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
  demo_Number = number_plate.detectMultiScale(img_read,1.1,5)
  for (x,y,w,h) in demo_Number:
    cv2.rectangle(img_read,(x,y),(x+w,y+h),(0,0,255),6)
    roi = img_read[y:y+h,x:x+w]
  st.Image(roi)
  st.Image(img_read)
if st.button('Number Plate Number'):
    Number = pytesseract.image_to_string(img_read)
    st.write(Number)
