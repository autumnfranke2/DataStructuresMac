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
    
    triageRoom.append(waitingRoom.pop(0))
    sorted(triageRoom, key = lambda x: x[2])
    print("Triage Room:", triageRoom)
    
    """nurse moves patient from triage room to exam room"""
    ExamRoom()
def enterWaitingRoom():
    waitingRoom.append((PatientInfo.name, PatientInfo.triageNumber,
                        PatientInfo.arrivalTime))
    print("Waiting Room:", waitingRoom)

def exit():
    examRoom.remove()

def ExamRoom():
        if len(examRoom) < 7 :
            examRoom.append(triageRoom.pop(0))
            print("Exam Room: ", examRoom)
        else:
            print("Triage Room:", triageRoom)


time.clock()
enterWaitingRoom()
callNurse()

