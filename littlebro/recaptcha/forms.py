from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm



class CaptchaLoginForm(AuthenticationForm):
    """
    Extends the login form to include a captcha field
    """
    captcha = ReCaptchaField(attrs={'theme': 'clean'})
