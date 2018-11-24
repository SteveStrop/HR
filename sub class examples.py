class Appointment(object):

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def done(self):
        pass


class PhotoAppointment(Appointment):

    def __init__(self, date, time, location):
        super(PhotoAppointment, self).__init__(date, time)
        self.location = location

    def start(self):
        pass


test = PhotoAppointment.time
test = PhotoAppointment.date
test = Appointment.time
test = Appointment.date
test = PhotoAppointment.A

