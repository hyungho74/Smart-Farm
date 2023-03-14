import cv2
capture = cv2.VideoCapture(0)
capture.set(3,640) #가로 길이 설정
capture.set(4,480) #세로 길이 설정
def gen():
    while True:
        ret, image = capture.read() #캠 화면을 읽어옴
        cv2.imwrite('t.jpg', image) #캠 화면을 .jpg형식으로 저장
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' +open('t.jpg', 'rb').read()+b'\r\n') #캠 영상을 프레임 단위로 전송
    capture.release()