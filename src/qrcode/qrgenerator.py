from src.qrcode.qrcode import *
from src.core.setcore import *
import os

# generate the qrcode and save it definition
def gen_qrcode(url):
    # generate the qrcode
    qr = QRCode(5, QRErrorCorrectLevel.L)
    qr.addData(url)
    qr.make()
    im = qr.makeImage()
    time.sleep(1)
    if os.path.isfile(setdir + "/reports/qrcode_attack.png"): os.remove(setdir + "/reports/qrcode_attack.png")
    # save the image out
    im.save(setdir + "/reports/qrcode_attack.png", format='png')
    # print that its been successful
    print_status("QRCode has been generated under %s/reports/qrcode_attack.png!" % (setdir))
