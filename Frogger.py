def frogger(well_height):
    days = 1
    jump = 4
    while well_height > 0:
        well_height = well_height - jump
        if well_height >= 0:
            well_height += 1
            days += 1

    return days

#This code takes checks how many days it takes for a frog with height zero to jump out of a well with a given height