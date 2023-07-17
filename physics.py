import numpy as np

# Global constants
g = 9.81  # m/s^2
density_water = 1000  # kg/m^3
atmospheric_pressure = 101325  # Pa


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

    depth: current depth of the water in m(positive and negative inputs are valid)
    """

    return atmospheric_pressure + density_water * abs(depth) * g  # N / m^2


def calculate_acceleration(F, m):
    """
    Calculates linear acceleration given the force applied and the mass of an object

    F: force applied in N
    m: mass of the object in kg"""

    if m <= 0:
        raise ValueError("The object must have a positive mass")
    return F / m  # m/s^2


def calculate_angular_acceleration(tau, I):
    """
    Calculates angular accelration given the torque applied and the moment of inertia of an object

    tau: torque applied in N*m
    I: moment of inertia of the object in kg*m^2"""

    if I <= 0:
        raise ValueError("The object must have a positive moment of inertia")
    return tau / I  # m/s^2


def calculate_torque(F_magnitude, F_direction, r):
    """
    Calculate the torque given the magnitude of force applied on an object, its direction, and the distance from the axis of rotation

    F_magnitude: magnitude of the force applied in N, with a positive or negative sign denoting the direction of the force
    F_direction: direction of the force applied in degrees relative to the axis of rotation
    r: distance from the axis of rotation to where the force is applied in m"""

    return r * F_magnitude * np.sin(np.deg2rad(F_direction))  # N*m


def calculate_moment_of_inertia(m, r):
    """
    Calculate the moment of inertai of an object given its mass and distance from the axis of rotation to its center of mass

    m: mass of the object in kg
    r: distance from the axis of rotation to the object's center of mass in m"""

    if m <= 0 or r < 0:
        raise ValueError(
            "Object must have a positive mass, and the distance from the axis of rotation to the center of mass of the object must be positive"
        )
    return m * r**2  # kg*m^2


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    """
    Calculate the acceleration of an AUV given the magnitude and direction of the force exerted by the thruster, the mass and volume of the AUV, and the distance from the thruster to the center of mass of the AUV

    F_magnitude: magnitude of force applied by the thruster in N
    F_angle: angle of the thruster in rad, measured from the x-axis, with positive angles measured in the counter-clockwise direction
    mass(optional): mass of the AUV in kg; default value is 100 kg
    volume(optional): volume of the AUV in m^3; default values is 0.1 m^3
    thruster_distance(optional): distance from the center of mass of the AUV to the thrusters; default value is 0.5 m

    """
    if (
        (abs(F_angle) > np.pi / 6 or thruster_distance < 0)
        or (volume <= 0 or mass <= 0)
        or abs(F_magnitude) > 100.0
    ):
        raise ValueError(
            "Thrusters are unable to rotate beyond thirty degrees in either direction, thruster distance must be a positive quantity, volume and mass must be quantity, and thruster may only apply forces with a magnitude of less than 100 m"
        )
    return np.array([
        calculate_acceleration(F_magnitude * np.cos(F_angle), mass),
        calculate_acceleration(F_magnitude * np.sin(F_angle), mass),
    ])


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """
    Calculates the angular acceleration of an AUV given the magnitude and direction of the force applied, the inertia of the ROV, and the distance to the thruster from teh AUV's center of mass

    F_magnitude: magnitude of force applied by the thruster in N
    F_angle: angle of the thruster in rad, measured from the x-axis, with positive angles measured in the counter-clockwise direction
    inertia: moment of inertia of the object in kg*m^2
    thruster_distance(optional): distance from the center of mass of the AUV to the thrusters; default value is 0.5 m

    """

    if (thruster_distance < 0 or abs(F_angle) > np.pi / 6) or inertia <= 0:
        raise ValueError(
            "Thruster distance cannot be negative, the thruster may not rotate more than thirty degrees in either directions, and the moment of inertia of the AUV must be positive"
        )
    return calculate_angular_acceleration(
        calculate_torque(F_magnitude, np.rad2deg(F_angle), thruster_distance), inertia
    )


# More testing necessary
def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """
    Calculates the acceleration of the AUV in the 2-D plane given the forces applied by each of the four thrusters, the angle at which the thrusters are rotated, the angle at which the AUV is rotated, and the mass of the AUV

    T:  np.ndarray of the magnitude of forces applied by each of the four the thrusters in N
    alpha: angle of the thruster in rad
    theta: angle at which the AUV is rotated in rad relative to the global context
    mass(optional): mass of the AUV in kg , the default value is 100 kg
    """

    if mass <= 0:
        raise ValueError("The mass of the object must be a positive quantity")
    r_alpha = np.array(
        [
            [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
            [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
        ]
    )
    r_theta = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )
    return np.dot(r_theta, np.dot(r_alpha, T)) / mass


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """
    Calculate the angular acceleration of the AUV given the forces applied by each of the four thrusters, the angle at which the thrusters are rotated, the angle at which the AUV is rotated, the dimensions of the AUV, and the rotational inertia of the AUV

    T:  np.ndarray of the magnitude of forces applied by each of the four the thrusters in N
    alpha: angle of the thruster in rad
    theta: angle at which the AUV is rotated in rad relative to the global context
    L: distance from the center of mass of the AUV to the thrusters on the major axis of the AUV in m
    l: distance from the center of mass of the AUV to the thrusters on the minor axis of the AUV in m
    inertia(optional): rotational inertia of the AUV, measured in kg*m^2
    """

    if (l < 0 or L < 0) or inertia <= 0:
        raise ValueError(
            "Dimensions of the AUV cannot be negative quantities, and the inertia must be a positive quantiti=y"
        )
    r_rotation = np.array([1, -1, 1, -1])
    sin_gamma = L * np.sin(alpha) + l * np.cos(alpha)
    return np.sum(np.multiply(r_rotation, T) * sin_gamma) / inertia


# Test 9 Debugging

print(calculate_auv2_acceleration(np.array([1.0, 3.0, 1.0, 2.0]), 0.5, 0.3))
print(
    calculate_auv2_angular_acceleration(np.array([1.0, 3.0, 1.0, 2.0]), 0.5, 1.5, 1.8)
)

"""
Expected Output:
[ 0.00980067 -0.00198669]
-0.06896360757926927
"""
