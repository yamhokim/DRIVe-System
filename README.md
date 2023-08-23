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


## Description of Files:

# How to Use:

