
import barcode
from barcode.writer import ImageWriter

# Take input from the user
data = input("Enter text or number to generate barcode: ")

# Generate Code 128 barcode
barcode_class = barcode.get_barcode_class("code128")

barcode_image = barcode_class(
    data,
    writer=ImageWriter()
)

# Save barcode image
filename = barcode_image.save("generated_barcode")

print("\nBarcode generated successfully!")
print("Barcode Data:", data)
print("Saved File:", filename)
