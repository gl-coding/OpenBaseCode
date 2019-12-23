import datetime

def get_cur_date_str():
    now  = datetime.datetime.now()
    strf = now.strftime('%d-%m-%Y %H:%M:%S')
    return strf

def get_date(): 
    date = datetime.date(2018, 8, 23)
    print(date)

def get_tomorrow():
    day_interval = datetime.timedelta(days=1)
    now  = datetime.datetime.now() + day_interval
    strf = now.strftime('%d-%m-%Y %H:%M:%S')
    print strf

def get_yestoday():
    day_interval =  datetime.timedelta(days=-1)
    now  = datetime.datetime.now() + day_interval
    strf = now.strftime('%d-%m-%Y %H:%M:%S')
    print strf

def get_timestamp():
    now = datetime.datetime.now()
    time = datetime.datetime.timestamp(now)
    print(time)

if __name__ == "__main__":
    get_date()
    get_tomorrow()
    get_yestoday()
