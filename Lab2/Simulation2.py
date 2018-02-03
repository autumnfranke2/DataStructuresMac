import random
names = ["Joey", "Bobby", "Sueann", "Loretta", "Grant",\
         "Genny", "Billy", "Tucker", "Cletus", "Hunter"\
         "Gunner", "Rose", "Amy", "Charlette", "Duke", \
         "Ricky", "Bo", "Luke", "Jesse"]

waitingRoom = []

triageRoom = []

examRoom = []
examRoomSize = 6
doctors = 6


def callNurse():
    """move patient from waiting room to triage room"""
    triageRoom.append(waitingRoom.pop(0))
    sort(triageRoom, key = patient.triageNumber)

    """nurse moves patient from triage room to exam room"""
    ExamRoom()


class Patient:
    def __init__(self):
        self.triageNumber = random.randint(0,100)
        self.name = names[random.randint(0,len(names)-1)] \
                    + " " + names[random.randint(0,len(names)-1)]
        self.arrivalTime = time.clock()
        self.treatmentTime = random.randrange(15,20)

    def enterWaitingRoom(self):
        waitingRoom.append(self.name)

    def exit(self):
        examRoom.remove(self.name)



def ExamRoom(self):
    if examRoom <= 6:
        examRoom.append(triageRoom.pop(0))
    else:
        null

   
def DocOffice():
    
    PatientName = self.name()
    PatientNumber = self.triageNumber()
    PatientArrival = self.arrivalTime()   
    time.clock()
    print(PatientName, PatientNumber, PatientArrival)


    
    
