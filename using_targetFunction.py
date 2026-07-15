import time
import threading

def sendSMS():
    time.sleep(4)
    print("SMS sent successfully!")

def sendEmail():
    time.sleep(2)
    print("Email sent successfully!")

def calculateETA():
    time.sleep(3)
    return "x minutes"  


if __name__ == "__main__":
    sms=threading.Thread(target=sendSMS)
    email=threading.Thread(target=sendEmail)
    eta=threading.Thread(target=calculateETA)

    sms.start()
    email.start()
    eta.start()

    sms.join()
    email.join()
    eta.join()

    print("All tasks completed successfully!")