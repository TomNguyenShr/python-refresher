# Problem 1
def calculate_buoyancy(V, density_fluid):
    g = 9.81
    return g * V * density_fluid


# Problem 2
def will_it_float(V, mass):
    g = 9.81
    if calculate_buoyancy(V, mass / V) > mass * g:
        return True
    elif calculate_buoyancy(V, mass / V) < mass * g:
        return False
    else:
        return True


# Problem 3
def calculate_pressue(depth):
    g = 9.81
    density = 1000
    return g * density * depth


# Problem 4
def calculate_acceleration(F, m):
    return F / m


# Problem 5
def calculate_angular_acceleration(tau, I):
    return tau / I


# Problem 6
def calculate_torque(F_magnitude, F_direction, r):
    torque = F_magnitude * r
    if F_direction > 180:
        torque = torque * -1
    return torque


# Problem 7
def calculate_moment_of_inertia(m, r):
    return m * r * r


# Problem 8
def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    calculate_acceleration(F_magnitude, mass)


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    torque = calculate_torque(F_magnitude, F_angle, thruster_distance)
    return calculate_angular_acceleration(torque, inertia)


def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    
    return
