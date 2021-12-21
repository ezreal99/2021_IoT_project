import picamera
import time

path = '/home/pi/src4/06_multimedia'
camera = picamera.PiCamera()

try:
    camera.resolution = (640,480)
    camera.start_preview()
    while True:
        val = input('photo:1, video:2, exit:9 > ')
        if val=='1':
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo_%s.jpg' % (path,now_str))
            print('사진 촬영')
        elif val=='2':
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/video_%s.h264' %(path,now_str))
            input('press enter to stop recording..')
            camera.stop_recording()
            print('동영상 촬영')
        elif val=='9':
            break
        else:
            print('incorrect command')

finally:
    camera.stop_preview()