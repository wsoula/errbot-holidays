from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
from datetime import datetime
import holidayapi
import os

class Holidays(BotPlugin):
    """Get Holidays"""

    @arg_botcmd('-y', type=int, dest='year', default=0)
    @arg_botcmd('-m', type=int, dest='month', default=0)
    @arg_botcmd('-d', type=int, dest='day', default=0)
    def holiday(self, msg, year, month, day):
        if year == 0:
            year = int(datetime.now().strftime('%Y'))-int(os.getenv('YEAR_OFFSET'))
        if month == 0:
            month = datetime.now().strftime('%m')
        if day == 0:
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
