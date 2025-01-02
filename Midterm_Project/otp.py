import pyotp
import qrcode

# secret_key = pyotp.random_base32()
# print(secret_key)
secret_key = '24ZLU6I7ZNXIJP6ZFDGFOKTFIYVCN5K3'
totp = pyotp.TOTP(secret_key)

def check_otp(otp):
    if totp.verify(otp, valid_window=1):
        return True

def show_qr():
    gg_uri = totp.provisioning_uri(name='test@gmail.com', issuer_name='test gg auth')
    qr = qrcode.make(gg_uri)
    qr.show()