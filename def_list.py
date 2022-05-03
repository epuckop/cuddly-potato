import datetime

def timecheck(tokentime, timelimit):
    def_currentTime = datetime.datetime.now()
    def_dateofmessage = datetime.datetime.fromtimestamp(int(tokentime)).replace(second=0, microsecond=0)
    def_timelimit = timelimit
    print(f"Message time:{def_dateofmessage}\nCurrent time:{def_currentTime}")
    if def_dateofmessage > def_currentTime:
        return False
    elif def_dateofmessage <= def_currentTime:
        def_timedifference = ((def_currentTime - def_dateofmessage).total_seconds() / 60)
        if def_timelimit > def_timedifference:
            print("Token is up to date")
            return True
        elif def_timelimit <= def_timedifference:
            print("Need to update token")
            return False
        else:
            return False
    else:
        return False
