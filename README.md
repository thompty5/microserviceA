# QR Code Generator Microservice

This microservice generates a QR code from text received in an HTTP GET request. The text is decoded and encoded into a QR code PNG image, which is sent back to the main program.

## Communication Contract

### Requesting Data:

Your main program must send an HTTP GET request to the address and port listed below, and the text to be encoded into the QR code must be in the body of the request.

* Communication Pipe: `REST API`
* Address: `http://localhost:8080/encode`

**Example Call:**

```Python
# The communication pipe to our microservice
url = 'http://localhost:8080/encode'

# The text to be encoded into a QR code
raw_text = b'Sharing rocket coordinates...40.7484 N, 73.9857 W'

# Send an HTTP GET request with the text to be encoded
requests.get(url, data=raw_text).content
```

### Receiving Data:

The microservice will send a PNG image file with the QR code back to the main program. The main program just needs a way to store the image.

**Example Call:**


```Python
with open ('new_qrcode.png', 'wb') as file:
    file.write(requests.get(url, data=raw_text).content)
```

### UML Diagram showing how the main program and this microservice communicate
<img width="629" height="578" alt="image" src="https://github.com/user-attachments/assets/fd239354-5b84-487e-a782-3aa844aeb637" />
