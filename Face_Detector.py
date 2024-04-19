
# importando bibliotecas reconhecimento facial
import cv2
from cvzone.FaceDetectionModule import FaceDetector


video = cv2.VideoCapture(0) # variavel video recebe entrada imagem webcan
detector = FaceDetector() # recebe instancia fo facedetector

while True: 
    _,imagem = video.read() # extrai a img da webcan em tempo real
    imagem,bboxes = detector.findFaces(imagem,draw=True) # extrai img, bboxes que sao as cordenadas da face

    cv2.imshow('Resultado', imagem) # exibe imagem na tela
    if cv2.waitKey(1) == 27: # da sequencia nos freemes da imagem
        break
