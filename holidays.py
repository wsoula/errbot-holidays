from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
from datetime import datetime
import holidayapi
import os

class Holidays(BotPlugin):
    """Get Holidays"""

    @botcmd
    def holidays(self, msg, args):
        year = int(datetime.now().strftime('%Y'))-1
        month = datetime.now().strftime('%m')
        day = datetime.now().strftime('%d')
        holiday_api = holidayapi.v1(os.getenv('API_KEY'))
        holiday_parameters = {
            'country': 'US',
            'year': year,
            'month': month,
            'day': day
        }
        holidays = holiday_api.holidays(holiday_parameters)
        if 'holidays' in holidays:
            return holidays['holidays'][0]['name']
        else:
            return holidays
