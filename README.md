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

## General Overview of the System :

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

## Description of Files:


