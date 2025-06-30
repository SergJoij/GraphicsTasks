import cv2
import numpy as np

# my_photo = cv2.imread('b1f090dace93e1a52bd1afd7303a8b13.png')
# my_photo = cv2.imread('IMG_20190414_004000_1.jpg')
# my_photo = cv2.imread('jazik.png')
# my_photo = cv2.imread('jazik_1.png')
my_photo = cv2.imread('atkarsk2.jpg')


def size_of_photo():
    ph_width = int(my_photo.shape[1])  # ширина оригинала в пикселях
    ph_height = int(my_photo.shape[0])  # высота оригинала в пикселях
    return ph_width, ph_height


width, height = size_of_photo()
my_photo = cv2.resize(my_photo, (int(width * 2), int(height * 2)))

# median_image = cv2.medianBlur(my_photo, 5)
img_grey = cv2.cvtColor(my_photo, cv2.COLOR_BGR2GRAY)  # преобразовать изображение в формат оттенков серого

# зададим порог
thresh = 90  # 90 для 5, 100 для 4, 151 для 3, 80 для 1

# получим картинку, обрезанную порогом
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

# найдем контуры
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# создадим пустую картинку
img_contours = np.zeros(my_photo.shape)

# отобразим контуры
cv2.drawContours(img_contours, contours, -1, (255, 255, 255), 1)

cv2.imshow('res ' + str(thresh), img_contours)  # выводим итоговое изображение в окно
cv2.waitKey()
cv2.destroyAllWindows()
