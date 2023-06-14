import cv2
import time
import keyboard as ky
from detectCursorModule import handTracker
import tools

def run(showCameraStream= False, noClickGesture=False):
    ostools = tools.osTools()
    osname = ostools.getSys()
    print('==FlotingHand==\nYou are on '+osname)
    cap = cv2.VideoCapture(1)
    print("Loading the MediaPipe package..")
    tracker = handTracker()
    time.sleep(0.5)
    ostools.clearConsole()
    print("If you want to exit the program, press ESC+F globally or press CTRL+C in the Shell")
    if noClickGesture == False:
        print("====\nClickGesture activated!\nIf you want to hold the LeftMouse perform the 'handUp' gesture,\nor else it will make the LeftMouse dosent hold\n====")
    
    time.sleep(3)
    
    while True:
        if ky.is_pressed('esc') and  ky.is_pressed('f'):
            cv2.destroyAllWindows()
            print('program exited')
            ostools.clearConsole()
            exit()
        
        success,image = cap.read()
        imageFlip = cv2.flip(image, 1)
        image = tracker.handsFinder(imageFlip)
        lmList = tracker.positionFinder(imageFlip)
        if showCameraStream:
            cv2.imshow("FlotingHand",imageFlip)
        
        cv2.waitKey(1)

cv2.destroyAllWindows()