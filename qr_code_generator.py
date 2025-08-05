# QR Code Generator Microservice
# This program will receive text to be encoded into a QR code via an HTTP GET request
# It will encode the text into a QR code PNG image, and will send an HTTP response back with the image

from flask import Flask, request, send_file
import qrcode

# The name of the QR code image we will generate
filename = 'qrcode.png'

app = Flask(__name__)

@app.route('/encode', methods=['GET'])
def encode_text():
    # Decode the binary data into text
    decoded_text = request.data.decode('utf-8')

    # Print our decoded text just so we know it is correct
    print(f'Our decoded text is: {decoded_text}')

    # Create a QR code using our decoded text
    img = qrcode.make(decoded_text)
    img.save(filename)

    # Send the QR code to the main program
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
    