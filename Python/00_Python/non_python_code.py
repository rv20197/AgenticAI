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

