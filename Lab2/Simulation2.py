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

class Patient:
    def __init__(self):
        self.triageNumber = random.randint(0,100)
        self.name = names[random.randint(0,len(names)-1)] \
                    + " " + names[random.randint(0,len(names)-1)]
##        self.arrivalTime = time
##        self.treatmentTime = random.randrange(15,20)

    def exit(self):
        pass
        #remove patient from simulation
