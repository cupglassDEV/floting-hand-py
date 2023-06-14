import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the live stream mode:
def getResult(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='/path/to/model.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=getResult)


class detectGesture():
    
   with GestureRecognizer.create_from_options(options) as recognizer:
    def __init__(self):
        self.
        # i think i like the default value of ALL settings that configured default
    def findGesture(self, image):
           try:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
            gesture_recognition_result = recognizer.recognize_for_video(mp_image, image)
            recognizer.recognize_async(mp_image, int)
           except any:
              exit()

    