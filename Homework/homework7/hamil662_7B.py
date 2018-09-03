#CSCI 1133 Homework 7
#Denasia Hamilton
#Problem 7B


class Member():
    def __init__(self, instrument, player):
        self.instrument = instrument
        self.player = player

    def getInstrument(self):
        return self.instrument

    def getPlayer(self):
        return self.player

    def setInstrument(self, new_instrument):
        self.new_instrument = new_instrument

    def setPlayer(self, new_player):
        self.new_player = new_player

    def __str__(self):
        return str(self.player) + " plays " + str(self.instrument)

    def __eq__(self, rhand):
        if self.instrument.lower() == rhand.instrument.lower() and self.player.lower() == rhand.player.lower():
            return True
        else:
            return False

class Band():
    def __init__(self, name, member_list):
        self.name = name
        self.member_list = member_list

    def getBandName(self):
        return self.name

    def getPlayers(self):
        name_list = [ ]
        for x in self.member_list:
            name_list.append(x.getPlayer())
        return name_list

    def getInstruments(self):
        d = { }
        for x in self.member_list:
            if x.getInstrument() not in d:
                d[x.getInstrument()] = 1
            else:
                d[x.getInstrument()] += 1
        return d

    def addMember(self, member):
        self.member = member
        self.member_list.append(self.member)

    def removeMember(self, member):
        self.member = member
        for x in self.member_list:
            if self.member == x.getPlayer():
                self.member_list.remove(x)

    def __str__(self):
        string = "Members of " +  self.name + ": " + "\n"
        for x in self.member_list:
            string += "{0} plays {1}".format(x.getPlayer(), x.getInstrument()) + "\n"
        return string

    def findPlayer(self, player):
        self.player = player
        found = False
        for x in self.member_list:
            if self.player == x.getPlayer():
                found = True
                print (self.player + " plays " + x.getInstrument())
        if found is False:
            print (self.name + " does not have any players named " + player)

    def findInstrument(self, instrument):
        self.instrument = instrument
        found = False
        for x in self.member_list:
            if self.instrument == x.getInstrument():
                print (x.getPlayer() + " plays " + self.instrument)
                found = True
        if found is False:
            print (self.name + " does not have any " + self.instrument + " players ")
