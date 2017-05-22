import sys
import os

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient

number = sys.argv[2]
text = sys.argv[3]

print("Sending WhatsApp...")
print("Number: " + number)
print("Text: " + text)

package = 'com.android.chrome'
activity = 'com.google.android.apps.chrome.Main'
component = package + "/" + activity
uri = 'https://api.whatsapp.com/send?phone=' + number

device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)
device.startActivity(component=component, uri=uri)
vc.sleep(3)
device.type(text)
vc = ViewClient(device=device, serialno=serialno)
send = vc.findViewByIdOrRaise('com.whatsapp:id/send')
send.touch()
