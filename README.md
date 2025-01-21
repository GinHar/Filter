# Filter
This program takes a video and manipulated to highlight the edges.

!(https://raw.github.com/GinHar/Filter/blob/main/Video.mp4)
!(https://raw.github.com/GinHar/Filter/blob/main/Video_filter.mp4)

## Project.py
The code that manipulates the video. You give the video's path and the program separate the video in frames and save them as "Frame#.jpg"  as . After, the code takes all the frames and passes a Gaussian and a Sobel filter, and a treshold. Then, it saves all this  manipulated frames as "Photo#.jpg". Finally, it converts this manipulated frames in a video.

## Extract.py
There are some functions that take an image and give matrix with the intensities or vice versa. It can work with images in color or in black and white.

## Filters.py
There are some functions that takes an image which is passed through a filter.

## Video.mp4
It is a video that is used in the program.
