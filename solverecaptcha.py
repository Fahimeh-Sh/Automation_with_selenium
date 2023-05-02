import sys
import os
from twocaptcha import TwoCaptcha
def solveRecaptcha(sitekey,URL):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=URL)

    except Exception as e:
        print(e)

    else:
        return result