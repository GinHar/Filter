from Filters import convolution_rfft, Gauss, Sobel
from Extract import extract_intensities,create_image_from_intensity
from numpy import where, any, empty, array, arange, hstack,exp, polyfit, sqrt, std, sum, mean,diag, linspace,log, savetxt
from pylab import show, imshow, plot, scatter, xlabel, ylabel, legend, title, errorbar
import cv2
import os


# Video's path
video_path = "Video.mp4"
frame_number = 0

# Load the video with OpenCV
cap = cv2.VideoCapture(video_path)

#Create the folder
folder = "Frames"
os.makedirs(folder, exist_ok=True)

if not cap.isOpened():
    print("Error.")
    exit()

while True:
    # Read frame from video
    ret, frame = cap.read()
    
    if not ret:
        print("Finish with the video.")
        break
    
    frame_name = f"Frame"+str(frame_number)+".jpg"
    frame_number+=1
    
    # Full path to save the frame
    save_path = os.path.join(folder, frame_name)
    
    #Save the frame
    cv2.imwrite(save_path, frame)
    print(f"Frame save as: {frame_name}")




tamaño = array([[0]])
frame_number = 1

image_path = "Frame"+str(0)+".jpg"  # Image's path
I = extract_intensities(image_path)
    
#Gauss+Sobel
I = Gauss(I)
I = Sobel(I)
    
    
img1 = create_image_from_intensity(I)
img1.save('Photo'+str(0)+'.jpg')

video_name = 'video_filter.avi'
# Read the first image to obtain the resolution
image = cv2.imread('Photo'+str(0)+'.jpg')
height, width, _ = image.shape

# Create the object VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30  # FPS
out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

img = cv2.imread('Photo'+str(0)+'.jpg')
out.write(img)  # Write the image in the video

#Create the folder
folder = "Photos"
os.makedirs(folder, exist_ok=True)


for i in range(frame_number,cap.get(cv2.CAP_PROP_FRAME_COUNT)):
    img_path = os.path.join(folder, 'Photo' + str(i) + '.jpg')
    I = extract_intensities(image_path)
    
    #Gauss+Sobel
    I = Gauss(I)
    I = Sobel(I)

    #Threshold
    I = where(I >= 110, 255, 0)
    
    #Create the image, save the image and make the video
    img1 = create_image_from_intensity(I)
    img1.save(img_path)
    img = cv2.imread(img_path)
    out.write(img)  # Write the image in the video
    
