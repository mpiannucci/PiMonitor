from google.appengine.ext import db


class StatusReport(db.Model):
    '''Status Report entries with date, temperature, and humidity'''
    date = db.DateTimeProperty(auto_now_add=True)
    temperature = db.FloatProperty()
    humidity = db.FloatProperty()

def newReport(temperature, humidity):
    ''' File a recieved report into the datastore'''
    status = StatusReport()
    status.temperature = temperature
    status.humidity = humidity
    status.put()

def getAllReports():
    '''Return all of the Status Reports'''
    report_query = db.Query(StatusReport).order('-date')
    return report_query