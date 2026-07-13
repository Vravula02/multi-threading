import time

def sendSms():
    time.sleep(4)
    print("SMS sent successfully!")

def sendEmail():
    time.sleep(2)
    print("Email sent successfully!")

def calculateETA():
    time.sleep(3)
    return "x minutes"


def orderService():
    print("Order placed successfully!")
    sendSms()
    sendEmail()
    eta = calculateETA()
    print(f"Estimated time of arrival: {eta}")

if __name__ == "__main__":
    orderService()