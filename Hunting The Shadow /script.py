# Read the header data as binary
with open('header.txt', 'rb') as header_file:
    header_data = header_file.read()

# Read body.txt as binary data
with open('body.txt', 'rb') as body_file:
    body_data = body_file.read()

# Write the combined data into a BMP file
with open('output_image.bmp', 'wb') as bmp_file:
    bmp_file.write(header_data)
    bmp_file.write(body_data)

print("BMP image file created: output_image.bmp")