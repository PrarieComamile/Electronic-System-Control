# Electronic-system-control
This project is designed to automate everyday tasks performed on a computer with the push of a single button. The project is developed on a Linux platform.



# **Getting Started**



## **Prerequisites**;


To use this project, you'll need the following:
* An Arduino Uno board
* Three buttons
* One potentiometer
* Three resistors
* Jumper cables

## **Installation;**

1. Connect the buttons and potentiometer to the Arduino Uno board as per the circuit diagram provided in the project files.
2. Connect the Arduino Uno board to your computer using a USB cable.
3. Open the `system_control.ino` file in the Arduino IDE and upload it to the Arduino board.
4. Install the necessary libraries on your computer. (The project is developed on a Linux platform and requires the following libraries):
    * PySerial
    * alsaaudio
    * pyautogui
    
    You can install these libraries using the following command on your Linux terminal:
     ```shell

      pip install pyautogui
      pip install pyalsaaudio
      pip install pyserial

    ```
5. Download the project files and extract them to a folder on your computer.
6. Open the `main.py` file in a Python editor and modify the serial port name and other parameters as per your requirements.
7. Run the `main.py` file to start the program.


## **Usage**

To use the program, simply press one of the three buttons connected to the Arduino Uno. The Python script running on the computer will listen to the serial port for input and trigger the corresponding function. (You can change the function.)

The functions that can be triggered are:

   * Function 1: Open the Discord.
   * Function 2: System update.
   * Function 3: Open the Visual Studio Code.
   
The potentiometer can be used to control the volume of the computer. Turn it to the left to decrease the volume, and to the right to increase it.


## **Linux Compatibility**

This project was developed on a Linux platform, and as such, certain changes may need to be made to the Python code to ensure compatibility with Windows. For example, the serial port names differ between Linux and Windows, and this difference should be taken into account when modifying the Python code. Additionally, the libraries used in this project have been selected specifically for Linux, and may need to be modified for use on a Windows system.


**Circuit;**
----------------------------------
![3a9e385a-ff30-42d0-8384-34eebfbe12a7](https://user-images.githubusercontent.com/101043132/232245887-974e5908-037e-4886-b315-e1cd3929dcdb.jpeg)



## **Acknowledgments**

This project was inspired by the need to automate repetitive tasks on a computer. Special thanks to [Vibasdo](https://github.com/Vibasdo) and the developers of PySerial, PyAlsaAudio and Pyautogui for making this project possible.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PrarieComamile/electronic-system-control/blob/main/LICENSE) file for details.





