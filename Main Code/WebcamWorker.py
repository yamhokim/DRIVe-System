from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import cv2
import mediapipe as mp
import math
from EAR import EAR
from MAR import MAR
from WebcamVideoStream import WebcamVideoStream
import imutils

class WebcamWorker(QThread):

    def __init__(self, time_secs, ear_vals, mar_vals, ear_and_mar_vals, blink_list, yawn_list, temp_ear_data, temp_time_data, ear_threshold, ear_open_value, perclos_vals, dimensions):
        super().__init__()
        self.time_secs = time_secs
        self.ear_vals = ear_vals
        self.mar_vals = mar_vals
        self.ear_and_mar_vals = ear_and_mar_vals
        self.blink_list = blink_list
        self.yawn_list = yawn_list
        self.temp_ear_data = temp_ear_data
        self.temp_time_data = temp_time_data
        self.ear_threshold = ear_threshold
        self.ear_open_value = ear_open_value
        self.perclos_vals = perclos_vals
        self.start_thread = False   # Starts the webcam and shows the graph
        self.name_entered = False
        self.counter = 0            # Will not start the webcam and graph until the counter becomes 1
        self.signal_counter = 0     # Set up this counter so that the label values are only updated every 5 frames to improve readability
        self.rating_countdown_signal = 0    # Once the 5 second rating window starts, this signal will be set off and the message will be displayed
        self.remaining_seconds = 5  # Will be used for the label telling observers how much longer is left in the rating window
        self.dimensions = dimensions # This is the dimensions of the FeedLabel
        self.observer_rating_timer = QTimer()
        self.observer_rating_timer.timeout.connect(self.update_remaining_seconds)


    StopLogging = pyqtSignal(bool)

    def start_switch(self):
        if self.counter == 0:
            self.counter += 1
        self.start_thread = True


    def stop_switch(self):
        self.start_thread = False
        self.counter = 0
        self.StopLogging.emit(True)
    

    ImageUpdate = pyqtSignal(QImage)
    PlotUpdate = pyqtSignal(list, list)
    RatioLabelUpdate = pyqtSignal(str, str)
    PerclosLabelUpdate = pyqtSignal(str)
    StartMainTimer = pyqtSignal()   # Signals when to start the rating timer so that the intervals line up

    def run(self):
        while self.counter == 0 or self.name_entered == False:
            continue

        start1 = time.time()  
        start2 = time.time()  # For the perclos stuff

        if True:
            self.StartMainTimer.emit()  # Start the main timer for determining when to start rating
            print("timer signal emitted")

        mp_face_mesh = mp.solutions.face_mesh

        perclos = 0
        MAR_threshold = 0.7   # Customize to whatever you want/need
        blink_frame_counter = 0
        yawn_frame_counter = 0
        blink_frame_threshold = 1
        yawn_frame_threshold = 30
        scale = 30            # for purpose of scaling the video (zooming in/out)

        closed_frame_counter = 0
        total_frame_counter = 0
        interval_counter = 0

        # Initialize a face_mesh object
        face_mesh_images = mp_face_mesh.FaceMesh(static_image_mode=False, 
                                                refine_landmarks=True,
                                                max_num_faces=1,
                                                min_detection_confidence=0.5, 
                                                min_tracking_confidence=0.5)
        
        vs = WebcamVideoStream(src=0).start()
        
        if (vs.stream.isOpened() == False):
            print("There was an error opening the mp4 file")
            self.quit()

        else:
            with face_mesh_images as face_mesh:
                while (vs.stream.isOpened()):
                    if self.start_thread == False:
                        break
                    frame = vs.read() # read the frame
                    
                    if True:
                        start_time = time.time()

                        # All of this is for resizing the image
                        # ---------------------------------------------------------------
                        height, width, channels = frame.shape
                        centerX,centerY=int(height/2),int(width/3) #For laptop screen
                        #centerX,centerY=int(height/2),int(width/2)  # For desktop screen
                        radiusX,radiusY= int(scale*height/100),int(scale*width/100)
                        minX,maxX=centerX-radiusX,centerX+radiusX
                        minY,maxY=centerY-radiusY,centerY+radiusY
                        cropped = frame[minX:maxX, minY:maxY]
                        resized_cropped = cv2.resize(cropped, (width, height))
                        resized_cropped = imutils.resize(frame, width=700)
                        image = cv2.cvtColor(resized_cropped, cv2.COLOR_BGR2RGB)  
                        flippedImage = cv2.flip(image, 1)
                        # ---------------------------------------------------------------
                        
                        results = face_mesh.process(flippedImage)
                        right_eye_landmarks = [(0,33), (1,160), (2,158), (3,133), (4,153), (5,144)]     # coords to be used to calculate right EAR
                        left_eye_landmarks = [(0,362), (1,385), (2,387), (3,263), (4,373), (5,380)]     # coords to be used to calculate left EAR
                        mouth_landmarks = [(0,76), (1,41), (2,12), (3,271), (4,306), (5,403), (6,15), (7,179)]  # coords to be used to calculate MAR

                        right_counter = 0
                        left_counter = 0
                        mouth_counter = 0

                        if results.multi_face_landmarks == None:
                            current_time = time.time()
                            time_elapsed = current_time - start1
                            time_elapsed_temp = current_time - start2 # To be used for the PERCLOS stuff
                            self.time_secs.append(time_elapsed)
                            self.mar_vals.append(0)
                            self.ear_vals.append(0)
                            self.ear_and_mar_vals.append([time_elapsed, 0, 0, 0, 0])
                            self.blink_list.append(0)
                            self.yawn_list.append(0)
                            total_frame_counter += 1

                            # For the animation function
                            # --------------------------
                            self.temp_time_data.append(time_elapsed)
                            self.temp_ear_data.append(0)
                            #---------------------------

                            if self.rating_countdown_signal == 1:
                                cv2.putText(flippedImage, f"Time Remaining for Rating: {self.remaining_seconds} Sec(s)", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 2)

                            convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                            pic = convertToQtFormat.scaled(self.dimensions.width() * 25, self.dimensions.height() * 25, Qt.KeepAspectRatio)
                            self.ImageUpdate.emit(pic)
                            self.PlotUpdate.emit(self.temp_time_data, self.temp_ear_data)
                            self.PerclosLabelUpdate.emit(str(round(perclos, 4)))
                            self.signal_counter += 1
                            if self.signal_counter == 5:
                                self.RatioLabelUpdate.emit("N/A", "N/A")
                                self.signal_counter = 0

                        else:
                            blinked = 0 # value to keep track of whether the participant blinked, used for logging data into csv file
                            yawned = 0  # value to keep track of whether the participant blinked, used for logging data into csv file
                            for face_landmarks in results.multi_face_landmarks:
                                current_time = time.time()
                                time_elapsed = current_time - start1
                                time_elapsed_temp = current_time - start2
                                total_frame_counter += 1

                                right_eye_coord_list = []
                                if right_counter == 0:
                                    for place, idx in right_eye_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        right_eye_coord_list.append((loc_x, loc_y))
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                    right_counter = 1
                                else:
                                    for place, idx in right_eye_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        right_eye_coord_list[place] = (loc_x, loc_y)
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                rightEar = EAR(right_eye_coord_list)

                                left_eye_coord_list = []
                                if left_counter == 0:
                                    for place, idx in left_eye_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        left_eye_coord_list.append((loc_x, loc_y))
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                    left_counter = 1
                                else:
                                    for place, idx in left_eye_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        left_eye_coord_list[place] = (loc_x, loc_y)
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                leftEar = EAR(left_eye_coord_list)

                                mouth_coord_list = []
                                if mouth_counter == 0:
                                    for place, idx in mouth_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        mouth_coord_list.append((loc_x, loc_y))
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                    mouth_counter = 1
                                else:
                                    for place, idx in mouth_landmarks:
                                        loc_x = int(face_landmarks.landmark[idx].x * resized_cropped.shape[1])
                                        loc_y = int(face_landmarks.landmark[idx].y * resized_cropped.shape[0])
                                        mouth_coord_list[place] = (loc_x, loc_y)
                                        cv2.circle(flippedImage,(loc_x, loc_y), radius=1, color=(255,255,255), thickness=1)
                                mar = MAR(mouth_coord_list)      

                                avgEar = (rightEar + leftEar) / 2         
                            
                                self.time_secs.append(time_elapsed)
                                self.mar_vals.append(mar)
                                self.ear_vals.append(avgEar)

                                # For the animation function
                                # --------------------------
                                self.temp_ear_data.append(avgEar)
                                self.temp_time_data.append(time_elapsed)


                                # --------------------------

                                if self.rating_countdown_signal == 1:
                                    cv2.putText(flippedImage, f"Time Remaining for Rating: {self.remaining_seconds} Sec(s)", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 0), 2)
                                self.PerclosLabelUpdate.emit(str(round(perclos, 4)))
                                self.signal_counter += 1
                                if self.signal_counter == 5:
                                    self.RatioLabelUpdate.emit(str(math.ceil(mar*10000)/10000), str(math.ceil(avgEar*10000)/10000))
                                    self.signal_counter = 0

                                # Cases for determining PERCLOS
                                # -----------------------------------------
                                if avgEar < (0.3 * self.ear_open_value): # If the eye is 70%> closed, increment the closed frame counter by 1, along with the total frame counter
                                    closed_frame_counter += 1

                                if time_elapsed_temp >= 10:  # 1 minute has passed, we are finished the interval
                                    perclos = round(closed_frame_counter / total_frame_counter, 5) * 100
                                    self.perclos_vals.append((interval_counter, perclos))
                                    closed_frame_counter = 0
                                    total_frame_counter = 0
                                    interval_counter += 1
                                    start2 = time.time()
                                # -----------------------------------------

                                # Cases for Blinking and Yawning
                                # -----------------------------------------
                                if avgEar < self.ear_threshold and mar > MAR_threshold:
                                    blink_frame_counter += 1  
                                    yawn_frame_counter += 1

                                    if blink_frame_counter >= blink_frame_threshold:
                                        self.blink_list.append(1)
                                        blinked = 1
                                    else:
                                        self.blink_list.append(0)
                                        blinked = 0

                                    if yawn_frame_counter >= yawn_frame_threshold:
                                        cv2.putText(flippedImage, "Yawn!", (330, 450), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                                        self.yawn_list.append(1)
                                        yawned = 1
                                    else:
                                        self.yawn_list.append(0)
                                        yawned = 0

                                elif avgEar < self.ear_threshold and mar < MAR_threshold:
                                    blink_frame_counter += 1
                                    yawn_frame_counter = 0
                                    yawned = 0
                                    self.yawn_list.append(0)

                                    if blink_frame_counter >= blink_frame_threshold:
                                        self.blink_list.append(1)
                                        blinked = 1
                                    else:
                                        self.blink_list.append(0)
                                        blinked = 0

                                elif mar > MAR_threshold and avgEar > self.ear_threshold:
                                    yawn_frame_counter += 1
                                    blink_frame_counter = 0
                                    blinked = 0
                                    self.blink_list.append(0)
                                    if yawn_frame_counter >= yawn_frame_threshold:
                                        cv2.putText(flippedImage, "Yawn!", (330, 450), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                                        self.yawn_list.append(1)
                                        yawned = 1
                                    else:
                                        self.yawn_list.append(0)
                                        yawned = 0
                            
                                elif mar < MAR_threshold and avgEar > self.ear_threshold:
                                    yawn_frame_counter = 0
                                    blink_frame_counter = 0
                                    blinked = 0
                                    yawned = 0
                                    self.blink_list.append(0)
                                    self.yawn_list.append(0)

                                self.ear_and_mar_vals.append([time_elapsed, avgEar, mar, blinked, yawned]) 
                                # -----------------------------------------
                                
                            convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                            pic = convertToQtFormat.scaled(self.dimensions.width() * 28, self.dimensions.height() * 28, Qt.KeepAspectRatio)
                            self.ImageUpdate.emit(pic)
                            self.PlotUpdate.emit(self.temp_time_data, self.temp_ear_data)

        end_time = time.time()
        time_elapsed_total = end_time - start_time
        
        print("closing windows")
        vs.stop()
        cv2.destroyAllWindows()


    def start_rating_countdown(self):
        self.observer_rating_timer.start(1000)
        self.remaining_seconds = 5
        self.rating_countdown_signal = 1
    

    def reset_rating_countdown(self):
        self.rating_countdown_signal = 0

    
    def update_remaining_seconds(self):
        if self.remaining_seconds >= 0:
            self.remaining_seconds -= 1
        
        if self.remaining_seconds < 0:
            self.reset_rating_countdown()


    def set_modified_ear_threshold(self, ear_threshold):
        self.modified_ear_threshold = ear_threshold     # Set the ear threshold for the participant
        self.name_entered = True                        # Set this value to True, so that the camera can now turn on
        print("Modified EAR Threshold: ", self.modified_ear_threshold)
    

    def stop(self):
        self.ThreadActive = False
        self.quit()