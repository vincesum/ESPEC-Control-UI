from Tasks import Task
class Cycle(Task):
    def __init__(self, temp1, temp2, hours, minutes, seconds, totalCycles, taskName, db_id):
        self.temp1 = temp1
        self.temp2 = temp2
        self.hours = str(hours)
        self.minutes = str(minutes)
        self.seconds = str(seconds)
        self.durationInSeconds = (hours * 3600 + minutes * 60 + seconds)
        self.totalCycles = totalCycles
        self.taskName = taskName
        self.db_id = db_id
        return
