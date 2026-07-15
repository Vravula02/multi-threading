import time
import threading

class SendSMS(threading.Thread):
    def run(self):
        time.sleep(2)
        print("SMS sent successfully!")

class SendEmail(threading.Thread):
    def run(self):
        time.sleep(2)
        print("Email sent successfully!")

class CalculateETA(threading.Thread):
    def run(self):
        time.sleep(3)
        print("ETA calculated successfully!")

if __name__ == "__main__":
    sms_thread = SendSMS()
    email_thread = SendEmail()  
    eta_thread = CalculateETA()

    sms_thread.start()
    email_thread.start()    
    eta_thread.start()

    sms_thread.join()
    email_thread.join() 
    eta_thread.join()
    
    print("All tasks completed successfully!")

