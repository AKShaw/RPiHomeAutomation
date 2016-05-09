import socket
import picamera
import time

class Stream():
    def __init__(self):
        pass
    

    def stream(self):
        with picamera.PiCamera() as camera:
            camera.resoulution = (640, 480)
            camera.framerate = 24

            server = socket.socket()
            server.bind(("0.0.0.0", 8000))
            server.listen(0)

            conn = server.accept()[0].makefile("wb")
            try:
                camera.start_recording(conn, format="h264")
                camera.wait_recording(60)
                camera.stop_recording()
            finally:
                conn.close()
                server.close()
