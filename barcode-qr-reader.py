from pyzbar import pyzbar
import cv2

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=5)
    return image

def decode(image):
    # Decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # Draw the barcode
        image = draw_barcode(obj, image)
        # Print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data.decode('utf-8'))  # Decode bytes to string
        print()
    return image, decoded_objects

if __name__ == "__main__":
    # Path to the image file
    image_path = "barcode1.png"

    # Read the image from the specified path
    image = cv2.imread(image_path)
    print(image)

    if image is None:
        print("Error: Unable to read the image. Please check the path.")
    else:
        # Decode detected barcodes & get the image that is drawn
        image, decoded_objects = decode(image)

        # Show the image in a window
        cv2.imshow("Barcode/QR Code Detector", image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
