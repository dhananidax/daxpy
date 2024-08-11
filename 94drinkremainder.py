# import win10toast 
'''from win10toast import ToastNotifier 

# create an object to ToastNotifier class 
n = ToastNotifier() 

n.show_toast("GEEKSFORGEEKS", "You got notification", duration = 10, 
icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico") '''

'''from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "Notification",
    "Notification body",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
)
'''

#github
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hello Dax!",
                   "Python is 10 seconds awsm!",
                   icon_path="custom.ico",
                   duration=10)

toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
