# QR Code Generator Microservice
# This program will receive text to be encoded into a QR code via an HTTP GET request
# It will encode the text into a QR code PNG image, and will send an HTTP response back with the image

import requests
import qrcode

# The communication pipe from our main program
source_url = 'http://localhost:8080/encode'
# The communication pipe to our main program
destination_url = 'http://localhost:8080/qrcode'
# The name of the QR code image we will generate
filename = 'qrcode.png'

# Get the binary data from the main program
response = requests.get(source_url)
if response.status_code == 200:
    try:
        # Decode the binary data into text
        decoded_text = response.content.decode(encoding='utf-8')

        # Print our decoded text just so we know it is correct
        print(f'Our decoded text is: {decoded_text}')

        # Create a QR code using our decoded text
        img = qrcode.make(decoded_text)
        img.save(filename)

    # Open our created image and post it for our main program
        with open(filename, 'rb') as file: # Replace 'example.png' with your image file
            files = {'image_file': file}
            response = requests.post(destination_url, files=files)

    except UnicodeDecodeError:
        # There was an error while trying to decode the text
        print('ERROR: The data could not be decoded as UTF-8.')

else:
    print(f'The request failed with status code: {response.status_code}')
