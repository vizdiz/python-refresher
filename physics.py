g = 9.81  # m/s^2
density_water = 1000  # kg/m^3


def calculate_buoyancy(density_fluid, v):
    """
    Calculates the buoyant force acting oon an object

    density_fluid: density of a fluid in kg/m^3
    v: volume of an object in m^3
    """
    if density_fluid <= 0 or v <= 0:
        raise ValueError("Density and volume must be positive quantities")
    return density_fluid * v * g  # N


def will_it_float(V, mass):
    """
    Determines if an object will float in water

    V: volume of an oject in m^3
    mass: mass of an object in kg
    """
    if mass <= 0 or V <= 0:
        raise ValueError("Mass and volume must be positive quantities")
    return (mass / V) < density_water


def calculate_pressure(depth):
    """
    Determines the pressure at a given depth

    depth: current depth of the water in m
    """

    return density_water * abs(depth) * g  # N / m^2
