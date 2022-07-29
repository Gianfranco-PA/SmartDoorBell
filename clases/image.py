import cv2

class Capture_image:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def capture(self):
        cap=cv2.VideoCapture(0)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.height)

        ret,frame=cap.read()
        cap.release()
        retval, buffer =cv2.imencode('.jpg', frame)
        
        return buffer