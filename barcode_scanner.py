
import cv2

# Connect pyzbar to the Homebrew ZBar library
from pyzbar import zbar_library

zbar_library.find_library = lambda name: "/opt/homebrew/opt/zbar/lib/libzbar.dylib"

from pyzbar.pyzbar import decode

print("===== BARCODE SCANNER =====")

image_path = input("Enter barcode image path: ").strip()

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    barcodes = decode(image)

    if barcodes:
        print("\nBarcode detected successfully!")

        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            print("Barcode Data:", data)
            print("Barcode Type:", barcode_type)

            # Draw rectangle around barcode
            x, y, w, h = barcode.rect

            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

            cv2.putText(
                image,
                data,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        cv2.imshow("Barcode Scanner", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("\nNo barcode detected!")
