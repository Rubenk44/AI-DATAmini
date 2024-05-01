import sounddevice as sd
from scipy.io.wavfile import write
import cv2



def audio():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
    
def billede():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('image.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()

    
def main():
    audio()
    billede()
    
main()