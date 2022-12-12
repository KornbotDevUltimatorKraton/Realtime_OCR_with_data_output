import cv2
import pytesseract

# Initialize the video capture object
video_capture = cv2.VideoCapture(2)

while True:
    # Get the next frame from the video stream
    success, image = video_capture.read()

    # Check if the frame was successfully read
    if not success:
        break

    # Run tesseract OCR on the image
    text = pytesseract.image_to_string(image)

    # Print the OCR text
    print(text)

    # Show the frame
    cv2.imshow('Video', image)
    #print(image)
    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object
video_capture.release()
