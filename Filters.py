from numpy import array,sqrt, pad
from numpy.fft import rfft2, irfft2

"""
Here there are four functions:

convolution_rfft is a function that takes an image and a filter an make the convolution between both.
Sobel is a function that takes an image and applies a Sobel filter
Gauss is a function that takes an image and applies a Gauss filter
Scharr is a function that takes an image and applies a Scharr filter
"""

def convolution_rfft(image, kernel):
    # Obtain the shape of the image and the kernel
    height, width = image.shape
    k_height, k_width = kernel.shape

    # Calculate the shape for the FFT
    output_shape = (height + k_height - 1, width + k_width - 1)
    
    # Zero-pad to the image and filter
    padded_image = pad(image, ((0, k_height - 1), (0, k_width - 1)), mode='constant')
    padded_kernel = pad(kernel, ((0, output_shape[0] - k_height), (0, output_shape[1] - k_width)), mode='constant')

    # Calculate the FFT
    fft_image = rfft2(padded_image)
    fft_kernel = rfft2(padded_kernel)

    # Multiply in the frecuency domain
    fft_result = fft_image * fft_kernel

    # Calculate the IFFT to obtain the convolution
    result = irfft2(fft_result)

    # Return the new image
    return result[:height, :width]


#Sobel filter
def Sobel(image):
    #Sobel Kernel
    kx = array([[-1,0,+1],
            [-2,0,+2],
            [-1,0,+1]])

    ky = array([[-1,-2,-1],
            [0,0,0],
            [+1,2,+1]])
    # Apply the convolution to the filters
    gradiente_x = convolution_rfft(image, kx)
    gradiente_y = convolution_rfft(image, ky)
    
    # Calculate the gradient's magnitude
    magnitude = sqrt(gradiente_x**2 + gradiente_y**2)
    
    return magnitude


#Gaussian filter
def Gauss(image):
    #Kernel
    Gauss = 1/159*array([[2,4,5,4,2],
                    [4,9,12,9,4],
                    [5,12,15,12,5],
                    [4,9,12,9,4],
                    [2,4,5,4,2]])
    # Apply the convolution to the filter
    result = convolution_rfft(image, Gauss)
    return result


#Scharr Filter
def Scharr(image):
    #Kernel Scharr
    sx = array([[3,0,-3],
            [10,0,-10],
            [3,0,-3]])

    sy = array([[3,10,3],
            [0,0,0],
            [-3,-10,-3]])
    # Apply the convolution to the filters
    gradiente_x = convolution_rfft(image, sx)
    gradiente_y = convolution_rfft(image, sy)
    
    # Calculate the gradient's magnitude
    magnitude = sqrt(gradiente_x**2 + gradiente_y**2)
    
    return magnitude









