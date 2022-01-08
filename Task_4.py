from os import name
import sys

class Team: # Class which store all the information of the team
    def __init__(self):
        self.name = ""
        self.played = 0
        self.wins = 0
        self.draw = 0
        self.loss = 0
        self.score = 0
        self.conceded = 0
        self.goal_diff = 0
        self.points = 0

    def getTeam_name(self): # getter function to get the name of the team
        return self.name 

    def setTeam_name(self, team_name): # setter function to set the name of the team
        self.name = team_name

    def update(self, score, conceded): # function to update the goals, played, draws, pts etc
        diff = score - conceded
        if diff >= 1:
            self.wins += 1
            self.points += 3
        elif diff < 0:
            self.loss += 1
        else:
            self.draw += 1
            self.points += 1
        self.played += 1
        self.goal_diff += diff
        self.score += score
        self.conceded += conceded
        
    def getStat(self): # Function to get all the stats in the list
        return [self.name, self.played, self.wins, self.draw, self.loss, self.score, self.conceded, self.goal_diff, self.points]


# Four Function is made as there are 4 teams
t1 = Team()
t2 = Team()
t3 = Team()
t4 = Team()

team_list  = list((t1, t2, t3, t4)) # Storing the team object in the list
t = open('C:\\Users\Surunga Education\Documents\Python_Class\Assessment\Team.csv')

for lines in t: # Getting the name of the team and storing in the team objects
    lines=lines.rstrip("\n")
    for i in team_list:
        if i.getTeam_name() == "":
            i.setTeam_name(lines)
            break
t.close()

result = open("C:\\Users\Surunga Education\Documents\Python_Class\Assessment\Result.csv") # Reading the games result

for lines in result: # Updating the stats one by one
    game = lines.split(",")
    for i in team_list:
        if game[0] == i.getTeam_name():
            i.update(int(game[1]), int(game[3]))
            break

    for i in team_list:
        if game[2] == i.getTeam_name():
            i.update(int(game[3]), int(game[1]))
            break
result.close()
    
result = []
for i in team_list: 
    result.append(i.getStat())

# Sorting the result by the pts, g.d. and score
result.sort(key = lambda row : (row[8], row[7], row[5]), reverse=True)

if len(sys.argv) != 1:
    print(sys.argv[1])
    print(len(sys.argv[1])*"=")

print(f"{'Name':<9} {'P':<2} {'W':<2} {'D':<2} {'L':<2} {'S':<3} {'C':<3} {'G.D.':<4} {'Pts.':<4}")

for i in result:
    print(f"{i[0]:<9} {i[1]:<2} {i[2]:<2} {i[3]:<2} {i[4]:<2} {i[5]:<3} {i[6]:<3} {i[7]:<4} {i[8]:<4}")
