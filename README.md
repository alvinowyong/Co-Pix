# Co-Pix
Communication facilitation device for learners

# Set-up

This project is assumes the utilisation of a Raspberry Pi. The version used Raspbian version 11 (bullseye). 

1. Clone this repository
2. Run the following commands in terminal:

```
    sudo apt-get install portaudio19-dev python3-pil python3-pil.imagetk flac python3-picamera
    pip install opencv-python python-dotenv SpeechRecognition azure-storage-blob pipwin pillow PyAudio
    pip3 install --user picamera
```
3. Run ``sudo raspi-config``
4. Navigate to Interface Options and select Legacy Camera and enable it.
5. Reboot your Raspberry Pi again.
6. Run ``vcgencmd get_camera``. If your camera is working, the output should be ``supported=1 detected=1``
7. To test if the camera is working, run ``raspistill -o image.jpeg``. This should result in a short period where the camera is activated.

