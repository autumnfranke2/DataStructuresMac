import random
import time

names = ["Joey", "Bobby", "Sueann", "Loretta", "Grant",\
         "Genny", "Billy", "Tucker", "Cletus", "Hunter",\
         "Gunner", "Rose", "Amy", "Charlette", "Duke", \
         "Ricky", "Bo", "Luke", "Jesse"]

waitingRoom = []

triageRoom = []

examRoom = []

examRoomSize = 6
doctors = 6


class Patient:
    def __init__(self):
        self.triageNumber = random.randint(0,100)
        self.name = names[random.randint(0,len(names)-1)] \
                    + " " + names[random.randint(0,len(names)-1)]
        self.arrivalTime = time.clock()
        self.treatmentTime = random.randrange(15,20)
        

PatientInfo = Patient()


def callNurse():
    from operator import itemgetter, attrgetter, methodcaller

    """move patient from waiting room to triage room"""
    
    if len(examRoom) < 7:
        examRoom.append(waitingRoom.pop(0))
        print("Exam Room: ", examRoom)
        TimeinExam()
    else:
        triageRoom.append(waitingRoom.pop(0))
        sorted(triageRoom, key = lambda x: x[2])
        print("Triage Room:", triageRoom)
        
    
    """nurse moves patient from triage room to exam room"""

def enterWaitingRoom():
    waitingRoom.append((PatientInfo.name, PatientInfo.triageNumber,
                        PatientInfo.arrivalTime))
    print("Waiting Room:", waitingRoom)


def TimeinExam():
    print(PatientInfo.treatmentTime)
    while (PatientInfo.treatmentTime > 0):
        PatientInfo.treatmentTime -= 1
        print(PatientInfo.treatmentTime)
    exit()
    print("Exam Room: ", examRoom)

def exit():
    examRoom.pop(0)


time.clock()
enterWaitingRoom()
callNurse()


