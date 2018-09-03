import turtle

class County():
    def __init__(self, c_name, c_pop):
        self.c_name = c_name
        self.c_pop = c_pop
        #slope and y-intercept using matrix equation
        m = (self.c_pop[0] * -1/7)+(self.c_pop[1] * -3/35)+(self.c_pop[2] * -1/35)
        self.m = m+(self.c_pop[3] * 1/35)+(self.c_pop[4] * 3/35)+(self.c_pop[5] * 1/7)
        self.m = float(format(self.m, ".4f"))
        b = (self.c_pop[0] * 11/21) + (self.c_pop[1] * 8/21) + (self.c_pop[2] * 5/21)
        self.b = b+(self.c_pop[3] * 2/21)+(self.c_pop[4] * -1/21)+(self.c_pop[5] * -4/21)
        self.b = float(format(self.b, ".4f"))
        #string of line y=mx+b
        self.regressionLine = "y = " + str(self.m) + "x +" + str(self.b)

    def __lt__(self, rhand):
        return self.m < rhand.m

    def display(self, y_max = 200):
        self.c_pop.sort()
        y_max = (500 / self.c_pop[5])
        self.point_list = [ ]
        for x in self.c_pop:
            self.point = int(x * y_max - 300)
            self.point_list.append(self.point)
        x_len = [-300,-190,-80,30,140,250]
        x = 0
        p = 0
        turtle.penup()
        #plotting points for population
        for i in self.c_pop:
            spot = x_len[x]
            turtle.goto(spot, self.point_list[p])
            turtle.write(i)
            turtle.dot("red")
            turtle.penup()
            x += 1
            p += 1
        d = 0
        q = 0
        #drawing regression line
        for i in range(len(self.c_pop)):
            spot2 = x_len[d]
            turtle.pencolor('red')
            line = self.m * i + self.b
            turtle.pendown()
            turtle.goto(spot2, self.point_list[q])
            q += 1
        l = self.point_list[5]
        turtle.penup()
        #labeling the regression line and county name
        turtle.goto(250, l + 10)
        turtle.write(self.regressionLine, font=("Times New Roman", 10, "bold"))
        turtle.goto(250, l + 30)
        turtle.write(self.c_name, font=("Times New Roman", 10, "bold"))

class State(County):
    #inheriting County function--will calculate self.m and self.b the same as County
    def __init__(self, s_name, s_pop, county_list):
        County.__init__(self, s_name, s_pop)
        self.c_name = s_name
        self.c_pop = s_pop
        self.county_list = county_list
        self.s_pop1 = s_pop

    def __lt__(self, rhand):
        return self.m < rhand.m

    def setScreen(self):
        #to view display
        turtle.setworldcoordinates(-350, -340, 450, 300)
        self.c_pop.sort()
        y_max = 500 / self.c_pop[5]
        self.point_list = [ ]
        for x in self.c_pop:
            self.point = int(x * y_max - 300)
            self.point_list.append(self.point)
        turtle.penup()
        turtle.goto(-310,-300)
        turtle.pendown()
        #creating ticks on x_axis at the year between -300 and 250
        x_len = [(-300, 2010),(-190,2011),(-80,2012),(30,2013),(140,2014),(250,2015)]
        for x,y in x_len:
            turtle.goto(x,-300)
            turtle.goto(x,-295)
            turtle.goto(x,-310)
            turtle.goto(x,-295)
            turtle.penup()
            turtle.goto(x,-320)
            turtle.write(y, align = "center")
            turtle.goto(x,-300)
            turtle.pendown()
        turtle.goto(260,-300)
        turtle.penup()
        turtle.goto(-300,-300)
        turtle.left(90)
        turtle.pendown()
        #creating ticks on y-axis for every quarter of 200, labeled by the population respectively
        quarters = [0.25,0.5,0.75,1]
        for i in quarters:
            turtle.goto(-300, 500 * i-300)
            turtle.write(int(self.c_pop[5] * i), align = "right")
            turtle.right(90)
            turtle.forward(10)
            turtle.right(180)
            turtle.forward(20)
            turtle.left(90)
            turtle.right(90)
            turtle.right(180)
            turtle.forward(10)
            turtle.right(90)
        turtle.goto(-300, self.point + 20)

    def display(self):
        self.setScreen()
        #plotting the points for s_pop
        x_len = [-300,-190,-80,30,140,250,2015]
        x = 0
        p = 0
        turtle.penup()
        for i in self.c_pop:
            spot = x_len[x]
            turtle.goto(spot, self.point_list[p])
            turtle.dot("blue")
            turtle.write(i)
            turtle.penup()
            x += 1
            p += 1
        d = 0
        l = 0
        #drawing linear regression line for state
        for i in range(len(self.s_pop1)):
            spot2 = x_len[d]
            turtle.pencolor('blue')
            line = self.m * i + self.b
            turtle.pendown()
            turtle.goto(spot2, self.point_list[l])
            l += 1
        turtle.penup()
        #labeling regression line and state name
        turtle.goto(250, 210)
        turtle.write(self.regressionLine, font=("Times New Roman", 10, "bold"))
        turtle.goto(250, 230)
        turtle.write(self.c_name, font=("Times New Roman", 10, "bold"))

class Analysis(State):
    def __init__(self,state_list):
        State.__init__(self, s_name, s_pop, state_list)
        self.state_list = state_list
        self.s_name = s_name
        self.s_pop = s_pop

    def displayState(self,name):
        for x in self.state_list:
            if name in x.c_name:
                x.display()

    def displayStateGreatestCounty(self,name):
        for x in self.state_list:
            if name in x.c_name:
                x.display() #doesn't display county

    def displayStateLeastCounty(self,name):
        for x in self.state_list:
            if name in x.c_name:
                x.display() #doesn't display county

    def clear(self):
        turtle.clearscreen()

    def greatestState(self):
        a_list = [ ]
        state_list = self.state_list
        while state_list:
            the_min = state_list[0]
            for x in state_list:
                if x < the_min:
                    the_min = x
            a_list.append(the_min)
            state_list.remove(the_min)
        i = len(a_list)
        highest = a_list[i-1] #texas
        return highest.c_name

    def leastState(self):
        a_list = [ ]
        state_list = self.state_list
        while state_list:
            the_min = state_list[0]
            for x in state_list:
                if x < the_min:
                    the_min = x
            a_list.append(the_min)
            state_list.remove(the_min)
        lowest = a_list[0] #west virgina
        return lowest.c_name

#parsing through file--floating
text_file = open("censusdata.csv","r")
county_list = [ ]
state_list = [ ]
#to ignore the first line in file, info is not needed
text_file.readline()

s_name = " "
s_pop = [ ]
c_pop = [ ]
isFirst = True
for line in text_file:
    line = line.strip("/n")
    line = line.split(",")

    if "County" in line[0]:
        c_name = line[0]
        for x in line[1:]:
            c_pop.append(int(x))
        #creating the County instances and appending to list
        c = County(c_name, c_pop)
        county_list.append(c)
        c_pop = [ ]
    else:
        if isFirst:
            s_name = line[0]
            for x in line[1:]:
                s_pop.append(int(x))
            isFirst = False
        else:
            #creating the State instances and appending to list
            s = State(s_name, s_pop, county_list)
            state_list.append(s)
            s_pop = [ ]
            s_name = line[0]
            for x in line[1:]:
                s_pop.append(int(x))
            county_list = [ ]

#creating Analysis instance to access methods
a = Analysis(state_list)
text_file.close()
