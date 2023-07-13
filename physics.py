g = 9.81  # m/s^2
density_water = 1000  # kg/m^3


def calculate_buoyancy(density_fluid, v):
    return density_fluid * v * g  # N


def will_it_float(V, mass):
    return (mass / V) < density_water


def calculate_pressure(depth):
    return density_water * abs(depth) * g  # N / m^2
