from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('2F635471583036423133653875524B4830364D5969674F67795877334148564973614732746A46483455383D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    # except APIException as e:
    #     res = e.decode('utf-8')
    #     print(res)
    # except HTTPException as e:
    #     res = e.decode('utf-8')
    #     print(res)


class IsAdminUserMixing(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
