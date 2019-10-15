'''
    this app is the camera interface
'''



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        faceCascade = cv2.CascadeClassifier('C:/Users/Rajneesh/Desktop/Project/frontalface.xml')
        faces=faceCascade.detectMultiScale(frame,scaleFactor=1.1,minSize=(40,40),minNeighbors=5,flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
            cv2.putText(frame,"Face", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0), 1, cv2.LINE_AA)
            
        #cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()

