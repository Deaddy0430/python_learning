managers={"Ethan", "David", "Phoebe"}
techs={"Ethan", "Zac", "Phoebe", "Kyle"}
print("Both manager and tech: ", managers & techs)
print("manager but not tech: ", managers - techs)
print("tech but not manager: ", techs - managers)
if "Phoebe" in managers:
    print("Phoebe is a manager")
else:
    print("Phoebe is not a manager")
print("Only takes one job: ", managers ^ techs)
print("Total empolyees: ", len(managers | techs))