## Title-
Automated-Security-System-Using-IoT-Version2.0

## Purpose of Project- 

To upgrade the traditional Reactive Surveillance System to Pro-Active Surveillance System by implementing real-time Face Detection, Face Recognition using Edge Computing.

## Description- 
The camera is made with Raspberry Pi 3B+ board, Raspberry Pi Camera Module V2, and 64 GB SD card. 
The idea is to convert the reactive surveillance system to a pro-active system by detecting and recognizing the faces of people in the controlled environment. 
If the face is detected and recognized (condition: Face should be 80% visible approx otherwise it will be considered as unknown i.e. potential threat)
The log is maintained with entries of present crowd. If the face is not recognized, the picture of the potential threat is sent to Security personal via email. 
The trainer to recognize the face has accuracy of more than 68% hence for lowering faulty outcomes, each face is scanned 3 times and then trigger the measures if required. 
The Camera is connected to the central system and implements edge computing, i.e. all the operations like face detection, recognition, alert generation, log maintenance are done on the local storage so the central system does not get affected with a higher number of cameras or heavy operations. 
The camera with all operations use 570 mAh power, connects to the internet via WiFi, and works on a simple 20000 mAh power bank for almost 24 hours. Hence making it more flexible on power-supply.