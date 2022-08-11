def eat_ghost(power_pellet_active, touching_ghost):
    return bool(power_pellet_active is True and touching_ghost is True)

def score(touching_power_pellet, touching_dot):
    return bool(touching_power_pellet is True or touching_dot is True)

def lose(power_pellet_active, touching_ghost):
    return bool(power_pellet_active is False and touching_ghost is True)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return bool(has_eaten_all_dots is True and (power_pellet_active is True or touching_ghost is False))
