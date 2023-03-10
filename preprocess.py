def if_cylinder_equal_four(cylindernumber):
    if cylindernumber == 4:
        return 1
    else:
        return 0

def convert_fuel_type(fuel_type):
    if fuel_type =="gas":
        return 1
    else:
        return 0

def convert_aspiration(aspiration):
    if aspiration =="turbo":
        return 1
    else:
        return 0

def convert_drivewheel(drivewheel):
    if drivewheel =="fwd":
        return [1,0]
    elif drivewheel =="rwd":
        return [0,1]
    else:
        return [0,0]

def convert_enginetype(enginetype):
    if enginetype =="dohcv":
        return [1,0,0,0,0]
    elif enginetype =="ohc":
        return [0,1,0,0,0]
    elif enginetype =="ohcf":
        return [0,0,1,0,0]
    elif enginetype =="ohcv":
        return [0,0,0,1,0]
    elif enginetype =="rotor":
        return [0,0,0,0,1]
    else:
        return [0,0,0,0,0]


## data is du=ictionary contains all input from the user
def preprocess_data(data):
    wheelbase = data["wheelbase"]
    curbweight = data["curbweight"]
    cylindernumber = data["cylindernumber"]
    enginesize = data["enginesize"]
    horsepower = data["horsepower"]
    highwaympg = data["highwaympg"]
    if_cylinder_four = if_cylinder_equal_four(data["cylindernumber"])
    fuel_type = convert_fuel_type(data["fueltype"])
    aspiration = convert_aspiration(data["aspiration"])
    drivewheel = convert_drivewheel(data["drivewheel"])
    enginetype = convert_enginetype(data["enginetype"])
    
    final_data = [wheelbase, curbweight, cylindernumber, enginesize, horsepower, highwaympg, if_cylinder_four , fuel_type , aspiration] + drivewheel + enginetype
    return final_data