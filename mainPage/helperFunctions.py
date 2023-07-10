from datetime import datetime



def datetime_to_int(dt=datetime.now()):
    formatted_date = dt.strftime("%d%m%y%H%M%S")
    return int(formatted_date)
