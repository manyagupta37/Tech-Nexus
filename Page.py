import qrcode
import os
os.system('pip install qrcode[pil]')
from PIL import Image
import json
waiting_list = [
    {"name": "Rajendra", "appointment_time": "10:00 AM"},
    {"name": "Vikramaditya", "appointment_time": "10:30 AM"},
    {"name": "Harshvardhan", "appointment_time": "11:00 AM"},
]

waiting_list_json = json.dumps(waiting_list, indent=4)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(waiting_list_json)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("doctor_waiting_list_qr.png")
img.show()