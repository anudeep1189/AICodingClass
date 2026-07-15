class Trace:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def getSkill(self):
        return self.skill


trace = Trace(
    "abc",
    ["Python", "ML", "NLU"]   #intializatrion 
)

print("Name:", trace.name)
print("Skills:", trace.getSkill())