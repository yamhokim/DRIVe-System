# Drowsiness Rating and Intervention Verification (DRIVe) System

Python-based application developed in collaboration with the Human Factors and Applied Statistics Lab (HFASt) Lab at the University Of Toronto. The application is a drowsiness rating system that presents a GUI in which observers can rate the drowsiness level of a driver, while given real-time eye tracking footage from an open-source computer vision library (OpenCV) and drowsiness metrics. The aim of the project is to provide researchers interested in studying driver behavior with an accessible and reliable way of testing system-initiated in-vehicle interventions.

It is recommended to interpret this code in Python Version 3.7 or higher, as earlier versions may not include the libraries required.

## Project Motivation:

- The recent massive increase in urbanization has resulted in the exponential increase in automobile use in recent years, subsequently leading to an increase in the number of road accidents and an all-time high in the number of fatalities related to transportation
- There are currently several driver monitoring systems (DMS) on the market, but a scoping review performed within the HFAST Lab revealed that a majority of research related to this sector focuses on the development of technology and neglects how the user will interact with the system and what interventions will be activated upon a successful detection of driver drowsiness
- Variations in the choice of grounds truths, a lack of consistency and standardization in the evaluation process, and general sensor and model issues indicate the need for more research in this specific area of study
- Providing researchers with an accessible and open-source research tool to conveniently test their own interventions will not only bring more light to this specific area of research but will also contribute to increasing road safety

## Description of Task:

The task and protocol were developed by Suzan Ayas. Studies have shown that participant observation as a research methodology, although not objective, can provide deeper and qualitative insights into human behavior and interaction (e.g. Qaddo, 2017). Two observers periodically rate the drowsiness level of a participant driving in a simulator environment. Below is the protocol:

| Rating  | Indicators|
| ------------- | ------------- |
| Not drowsy  | Appearance of alertness present; normal facial tone; normal fast eye blinks; short ordinary glances; occasional body movements/gestures |
| Slightly drowsy | Still sufficiently alert; less sharp/alert looks; longer glances; slower eye blinks; first mannerisms such as rubbing face/eyes, scratching, facial contortions, moving restlessly in the seat;  |
| Moderately drowsy | Eye-lid closures (1-2s); mannerisms; slower eye-lid closures; decreasing facial tone; glassy eyes; staring at fixed position; |
| Very drowsy | Eyelid closures (2-3s); eyes rolling upward / sideways; no proper focused eyes; decreased facial tone; lack of apparent activity; large isolated or punctuating movements;  |
| Extremely drowsy | Eyelid closures (4s or more); falling asleep; longer periods of lack of activity; movements when transition in and out of dozing;  |

Observers are to use the given data presented to them (Eye aspect ratio, Mouth aspect ratio, number of blinks, number of yawns, and facial tracking footage) to support their vote. Observers give one vote for every "phase" of the rating session, after a predetermined elapsed time. These phases are done in time intervals, and observers cannot vote for a specific interval once that time window has passed. 

## General Overview of the GUI :

Shown below is an image of the GUI that the observers will be interacting with. The GUI was created through the use of Python's PyQt5 library.

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/0b77e8e5-e472-4b49-9446-b048d61cb7af)

The GUI itself has three main features:

**Live Observer Rating System** :

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/77c67db7-e94a-40d2-a662-4c4668666639)

On the left of the GUI, we have a table with interactive buttons that provide each of the two observers with five different "drowsiness" states to choose from, ranging from ALERT all the way to EXTREMELY DROWSY. Once the "START" button is pressed, the rating portion of the system will begin, where the two observers will be periodically asked to rate the driver's state using one of the five options provided to them. The protocol behind choosing each of the states is provided to the users at any point by pressing the "INFO" button. Doing so will pop up this info screen:

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/22705502-fdec-4a78-b71f-74b88da67e6e)

Once the "STOP" button is pressed, the webcam will turn off, the graph will reset, and all data will be saved onto the database.

**Live Video Feed** :

The GUI also provides the observers with live webcam footage, showing the observers the physical state of the driver at any point during the duration of the experiment. When the system has not started, a simple camera icon will occupy this area. 

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/2a6788b6-5819-4105-921e-aed0ce1557e0)

Upon pressing the "START" button, the user will be prompted to fill in the information about the driver and then will be asked to complete a prerequisite stage where the modified eye aspect ratio (EAR) threshold of the driver will be calculated. Since facial features differ by person, the ear threshold will have to be made personal to each person. The user will press the "OPEN" button to get the EAR of the driver with their eyes in a natural open position, and the "CLOSED" button to get the EAR of the driver with their eyes in a closed position. Once both values have been logged, the system will calculate the EAR threshold for the driver, and the webcam footage will now occupy the area the camera icon previously held.

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/2409dfea-6219-4c8e-999f-92c8a792aa3d)

**Live Data Visualization** :

In addition, the system also provides live data visualization to assist the observers in making their final decisions. To the right of the webcam footage, there are three metrics that the system is specifically looking at: Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and Percentage of Eye Closure (PERCLOS). The system will be logging these values and providing real-time updates to the values shown in the label.

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/f4ad1121-661c-46a4-becf-e620fec93b1d)

Below this, there is an animated graph created using the PyQtGraph library which provides a real-time visual representation of the EAR value to the observers.

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/6e05b90e-ea52-4bf0-bed2-c1dd355f834e)

## General Overview of System Backend:

Aside from the GUI that the observers interact with, the system has multiple features running in the backend. For the drowsiness detection portion of the system, I decided to use a computer-vision-based method. The application builds upon Mediapipe's deep-learning-based facial landmark solution which provides accurate real-time detection and tracking of 468 individual facial landmarks. This was used in conjunction with Python's OpenCV library to read individual frames from the video feed, apply the facial landmark solution, localize the areas of interest (eyes, mouth, areas around both eyes and mouth), and calculate the specific metrics (EAR, MAR, PERCLOS). Below is a simple flowchart showing the backend functionality of this method:

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/301820e8-ba3f-48aa-9509-1d8200aac380)

To increase the FPS of the webcam while the system was running, I utilized Python multithreading by creating a new thread to handle the polling of the camera for new frames. This freed the main thread from taking on this task and instead allowed it to focus on the processing of the frames. This helped in increasing the FPS by around 40%. The code for this is found within the WebcamVideoStream.py file.

Multithreading was also used to ensure that both the webcam footage shown in the OpenCV window and the animated graph created through PyQtGraph could be shown simultaneously without blocking one another from updating.

**Description of Files** :
- **main.py**: Main file to run the application and start the program
- **MainWindow.py**: Main GUI window. Changes to event handling and timers are done in this file.
- **ui_new_drive_rating_gui.py**: Contains adding and styling of the interface widgets for the main GUI Window
- **ui_protocol_info.py**: Contains adding and styling of the widgets for the protocol GUI Window
- **ui_drive_splashscreen.py**: Contains adding and styling of the widgets for the splash screen GUI Window
- **WebcamWorker.py**: Python file that is threaded to run the eye and mouth tracking program alongside the GUI. EAR and MAR calculations and facial landmarking (for eye and mouth tracking) is executed through this file.
- **WebacamVideoStream.py**: Code for using OpenCV's video streaming methods to use the webcam and stream real-time or a prerecorded video file.
- **SplashScreen.py**: Contains adding and styling of the widgets for the Splashscreen GUI Window
- **PopUp.py**: Pop-up window PyQT class, for users to enter their name
- **PlotWindow.py**: PyQT Class for the window that shows the plots. 
- **EAR.py** and **MAR.py**: Calculations to get Eye Aspect Ratio and Mouth Aspect Ratio, based on frame data from webcam and facial landmarks from OpenCV
- **csv_writer.py**: Class for the CSV writer objects to write data to a .csv file
- **InfoPopUp.py**: PyQt Class for the window that pops up upon pressing the info button. Provides users with the protocol for the different states.
- **ThresholdCalculator.py**: Contains all backend functionality for the window where the modified EAR threshold is calculated.
- **ThresholdWorker.py**: QtThread object that runs the webcam footage when logging for open and closed-eye EAR to calculate the EAR threshold.
- **ui_modified_ear_threshold_window.py**: Contains adding and styling of the widgets for the threshold calculation window that occurs before the rating starts.

## How to Use:

- Running the **main.py** will start the program. A splash screen is shown, then the main GUI interface appears.

**Start**

- Observer is prompted to enter their name
- Upon entering the driver's name, the modified EAR threshold window will open where the user will have the press the "OPEN" and "CLOSED" buttons while the driver is opening and closing their eyes, respectively
- Upon getting the modified EAR threshold, the webcam stream will open and EAR plot window will appear. Real-time eye tracking and EAR plot updates will occur
- Every x minutes, the observers will need to rate the state of the driver, at which point a message will appear on top of the webcam footage informing how much time is left to make a decision
- After the message disappears, the ratings will be logged, and the cycle will repeat

**Info**

- The info button will open the protocol information in a seperate window

**Stop**

- The stop button will end real-time streaming and stop the rating session.
- Two CSV files and two PNG files will be outputted as a result of ending the program:
   1) {name of observer}-Data.csv : Tuples in the form of [Time (s),EAR, MAR, Blinked (Y/N), Yawned (Y/N)] is outputted for every frame since the beginning of the rating session
   2) {name of observer}-observer-ratings-{date}.csv: Tuples in the form [Interval #,Interval Start Time,Observer 1 Rating,Observer 2 Rating] is outputted for each rating interval during the session
   3) {name}-eyedata.png will show the plot of EAR and number of blinks throughout the rating session.
   4) {name}-mouthdata.png will show the plot of MAR and number of yawns throughout the rating session.

# Project Presentation Poster

![image](https://github.com/yamhokim/DRIVe-System/assets/116863345/9d636603-beca-4d65-9057-4d1f637491cc)
