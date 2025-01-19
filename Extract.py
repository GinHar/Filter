from PIL import Image
import numpy as np

def extract_rgb_matrices(image_path):
    # Cargar la imagen
    img = Image.open(image_path)
    
    # Convertir la imagen a un array de numpy
    img_array = np.array(img)

    # Extraer los canales R, G y B
    R = img_array[:,:,0]  # Canal rojo
    G = img_array[:,:,1]  # Canal verde
    B = img_array[:,:,2]  # Canal azul
    
    return R, G, B

def combine_rgb_matrices(R, G, B):
    # Verificar que las matrices tienen la misma forma
    if R.shape != G.shape or R.shape != B.shape:
        raise ValueError("Las matrices R, G y B deben tener la misma forma.")
    
    # Combinar las matrices en un solo array
    img_array = np.stack((R, G, B), axis=-1)
    
    # Convertir el array a tipo uint8
    img_array = img_array.astype(np.uint8)
    
    # Crear la imagen a partir del array
    img = Image.fromarray(img_array)
    
    return img

    """
    reconstructed_image.save('ruta/a/tu/nueva_imagen.jpg')
    """


def extract_intensities(image_path):
    # Cargar la imagen en escala de grises
    img = Image.open(image_path).convert('L')  # 'L' para convertir a escala de grises
    
    # Convertir la imagen a un array de numpy
    intensity_array = np.array(img)

    return intensity_array

def create_image_from_intensity(intensity_array):
    # Convertir la matriz de intensidades a tipo uint8
    intensity_array = intensity_array.astype(np.uint8)
    
    # Crear una imagen a partir del array
    img = Image.fromarray(intensity_array, mode='L')  # 'L' para imagen en escala de grises
    
    return img


############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################


