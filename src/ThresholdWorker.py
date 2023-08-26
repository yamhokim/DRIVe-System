import cv2
import mediapipe as mp
import imutils
from WebcamVideoStream import WebcamVideoStream
from EAR import EAR
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ThresholdWorker(QThread):

    def __init__(self, desktop_dimensions):
        super().__init__()

        self.desktop_dimensions = desktop_dimensions
        self.ear_vals = []
        self.stop_run = False   # When this signal is True, it means for the run() function to terminate
    

    def terminate_run(self):
        self.stop_run = True


    webcamSignal = pyqtSignal(QImage)

    def run(self):
        
        scale = 30  # For the purpose of zooming the video in and out

        mp_face_mesh = mp.solutions.face_mesh

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

                    if self.stop_run:   # The stop_worker_signal from ThresholdCalc has been emitted, so stop reading frames
                        break

                    frame = vs.read() # read the frame
                    
                    if True:

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

                        right_counter = 0
                        left_counter = 0

                        if results.multi_face_landmarks == None:
                            self.ear_vals.append(0)
                            convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                            pic = convertToQtFormat.scaled(int(self.desktop_dimensions.width() * 0.5), int(self.desktop_dimensions.height() * 0.5), Qt.KeepAspectRatio)
                            self.webcamSignal.emit(pic)
                            
                        else:
                            for face_landmarks in results.multi_face_landmarks:
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

                                avgEar = (rightEar + leftEar) / 2         
                                self.ear_vals.append(avgEar)

                            convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0], QImage.Format_RGB888)
                            pic = convertToQtFormat.scaled(int(self.desktop_dimensions.width() * 0.5), int(self.desktop_dimensions.height() * 0.5), Qt.KeepAspectRatio)
                            self.webcamSignal.emit(pic)
        
        print("closing threshold workers")
        #vs.stop()
        #cv2.destroyAllWindows()