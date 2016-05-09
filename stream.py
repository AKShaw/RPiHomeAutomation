import time
import socket
import picamera


class Stream():
    def __init__(self):
        pass

    def main(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 24
            
            server_socket = socket.socket()
            server_socket.bind(("0.0.0.0", 8000))
            server_socket.listen(0)
            
            connection = server_socket.accept()[0].makefile("wb")
            try:
                camera.start_recording(connection, format="h264")
                camera.wait_recording(60)
                camera.stop_recording()
            finally:
                connection.close()
                server.socket_close()

