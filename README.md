# Co-Pix
Communication facilitation device for learners

# Set-up

This project is assumes the utilisation of a Raspberry Pi. The version used Raspbian version 11 (bullseye). 

1. Clone this repository
2. Run the following commands in terminal:

```
    pip install opencv-python python-dotenv SpeechRecognition azure-storage-blob pipwin
    pipwin install pyaudio
    sudo apt-get install portaudio19-dev
    sudo apt-get install flac
```
3. Run ``sudo raspi-config``
4. Navigate to Interface Options and select Legacy camera to enable it.
5. Reboot your Raspberry Pi again.
6. Run ``vcgencmd get_camera``. If your camera is working, the output should be ``supported=1 detected=1``

