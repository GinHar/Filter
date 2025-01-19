from Filtros import convolucion_rfft, aplicar_gauss, aplicar_sobel
from Extract import extract_intensities,create_image_from_intensity
from numpy import where, any, empty, array, arange, hstack,exp, polyfit, sqrt, std, sum, mean,diag, linspace,log, savetxt
from pylab import show, imshow, plot, scatter, xlabel, ylabel, legend, title, errorbar
import cv2


#Guardamos los frames del vídeo
# Ruta del video
video_path = "Video.mp4"  # Cambia esto a la ruta de tu video
frame_number = 0

# Cargar el video con OpenCV
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video.")
    exit()

while True:
    # Leer frame del video
    ret, frame = cap.read()
    
    if not ret:
        print("Fin del video.")
        break
    
    frame_name = f"Frame"+str(frame_number)+".jpg"
    frame_number+=1
    cv2.imwrite(frame_name, frame)
    print(f"Frame guardado como: {frame_name}")




tamaño = array([[0]])
frame_number = 0

#Limitamos a 96 frames porque los errores a partir de ahí son muy grandes
for i in range(frame_number):
    image_path = "Frame"+str(i)+".jpg"  # Ruta de la imagen
    I = extract_intensities(image_path)
    
    #Gauss+Sobel
    I = aplicar_gauss(I)
    I = aplicar_sobel(I)
    
    
    img1 = create_image_from_intensity(I)
    img1.save('MM_III\Foto'+str(i)+'.jpg')
    