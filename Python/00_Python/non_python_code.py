def fill_kettle_with_water():
    raise NotImplementedError

def kettle_has_water():
    raise NotImplementedError

def plug_in_kettle():
    raise NotImplementedError

def boil_water():
    raise NotImplementedError

def is_cup_clean():
    raise NotImplementedError

def clean_cup():
    raise NotImplementedError

def add_to_cup(item):
    raise NotImplementedError

def pour(param1, param2):
    raise NotImplementedError

def stir(cup):
    raise NotImplementedError

def serve(beverage):
    raise NotImplementedError

def make_tea():
    if not kettle_has_water():
        fill_kettle_with_water()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        clean_cup()
    add_to_cup('tea leaves')
    add_to_cup('sugar')
    pour('boiled water', 'cup')
    stir("cup")
    serve("chai")

make_tea()

