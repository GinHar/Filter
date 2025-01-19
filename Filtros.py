from numpy import array,sqrt, pad
from numpy.fft import rfft2, irfft2



def convolucion_rfft(imagen, kernel):
    # Obtener las dimensiones de la imagen y del kernel
    altura, ancho = imagen.shape
    k_altura, k_ancho = kernel.shape

    # Calcular las dimensiones para la FFT
    output_shape = (altura + k_altura - 1, ancho + k_ancho - 1)
    
    # Zero-pad de la imagen y el kernel
    padded_imagen = pad(imagen, ((0, k_altura - 1), (0, k_ancho - 1)), mode='constant')
    padded_kernel = pad(kernel, ((0, output_shape[0] - k_altura), (0, output_shape[1] - k_ancho)), mode='constant')

    # Calcular la FFT de la imagen y el kernel
    fft_imagen = rfft2(padded_imagen)
    fft_kernel = rfft2(padded_kernel)

    # Multiplicar en el dominio de la frecuencia
    fft_resultado = fft_imagen * fft_kernel

    # Calcular la inversa de la FFT para obtener la convolución
    resultado = irfft2(fft_resultado)

    # Retornar solo la parte que corresponde a la imagen original
    return resultado[:altura, :ancho]


#Filtro Sobel
def aplicar_sobel(imagen):
    #Kernel Sobel
    kx = array([[-1,0,+1],
            [-2,0,+2],
            [-1,0,+1]])

    ky = array([[-1,-2,-1],
            [0,0,0],
            [+1,2,+1]])
    # Aplicar la convolución con los operadores de Sobel
    gradiente_x = convolucion_rfft(imagen, kx)
    gradiente_y = convolucion_rfft(imagen, ky)
    
    # Calcular la magnitud del gradiente
    magnitud = sqrt(gradiente_x**2 + gradiente_y**2)
    
    return magnitud


#Filtro Gaussiana
def aplicar_gauss(imagen):
    #Kernel de Suavizado
    Gauss = 1/159*array([[2,4,5,4,2],
                    [4,9,12,9,4],
                    [5,12,15,12,5],
                    [4,9,12,9,4],
                    [2,4,5,4,2]])
    # Aplicar la convolución con los operadores de Gauss
    suavizado = convolucion_rfft(imagen, Gauss)
    return suavizado


#Filtro Scharr
def aplicar_scharr(imagen):
    #Kernel Scharr
    sx = array([[3,0,-3],
            [10,0,-10],
            [3,0,-3]])

    sy = array([[3,10,3],
            [0,0,0],
            [-3,-10,-3]])
    # Aplicar la convolución con los operadores de Schar
    gradiente_x = convolucion_rfft(imagen, sx)
    gradiente_y = convolucion_rfft(imagen, sy)
    
    # Calcular la magnitud del gradiente
    magnitud = sqrt(gradiente_x**2 + gradiente_y**2)
    
    return magnitud









