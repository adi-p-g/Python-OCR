import cv2
import pytesseract
import numpy as np
import googletrans

from langdetect import detect
#from google_trans_new import google_translator

from googletrans import Translator
#import all_language

img = cv2.imread('Image in Spanish.jpg')
#Alternatively: can be skipped if you have a Blackwhite image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(img)
print("OUTPUT:", out_below)

language = googletrans.LANGUAGES
result_lang = detect(out_below)
print("\nDETECTED LANGUAGE IS ")
print(language[result_lang])

print("\n\nTRANSLATED SENTENCE TO ENGLISH: ")
target_lang = "en"
    
if result_lang == target_lang:
        print(out_below)
    
else:
        translator = Translator()
        translate_text = translator.translate(out_below,lang_src=result_lang,lang_tgt=target_lang)
        print(translate_text) 
