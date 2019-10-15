import cv2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''

        camera = self.ids['camera']
        img=cv2.VideoCapture(0)
        state,pix=img.read()
        faceCascade = cv2.CascadeClassifier('C:/Users/Rajneesh/Desktop/Project/frontalface.xml')
        faces=faceCascade.detectMultiScale(pix,scaleFactor=1.1,minSize=(40,40),minNeighbors=5,flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            cv2.rectangle(pix,(x,y),(x+w,h+y),(0,255,0),2)
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        



class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()



# img.read()
# state,pix=img.read()
# cv2.imshow('my_image',pix)
# cv2.imwrite('my_image.jpg',pix)
# for(x,y,w,h) in faces:
#     cv2.rectangle(pix,(x,y),(x+w,h+y),(0,255,0),2)
# cv2.imshow(str(len(faces))+'faces',pix)
# cv2.waitKey(0)
# img.release()
# cv2.destroyAllWindows()