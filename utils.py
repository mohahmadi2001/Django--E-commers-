from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI("684C69554C4641476F4F3066375177464E594B765271655541712F777942445467364E39464C556E67356F3D")
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'your verification code is {code}',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)