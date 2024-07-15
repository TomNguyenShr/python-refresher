import numpy as np
import math


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
    Perpen_F = F_magnitude * math.sin(F_direction / 180 * math.pi)
    torque = Perpen_F * r
    return torque


# Problem 7
def calculate_moment_of_inertia(m, r):
    return m * r * r


# Problem 8
def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if F_angle > math.pi / 6 or F_angle < -math.pi / 6:
        return "Angle has to be between 30 to -30 degree"
    Fx = F_magnitude * math.cos(F_angle)
    Fy = F_magnitude * -math.sin(F_angle)
    return (calculate_acceleration(Fx, mass), calculate_acceleration(Fy, mass))


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    torque = calculate_torque(F_magnitude, F_angle / math.pi * 180, thruster_distance)
    return calculate_angular_acceleration(torque, inertia)


# Problem 9
def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    Fy = math.sin(alpha) * (T[1] + T[2] - T[3] - T[0])
    Fx = math.cos(alpha) * (-T[1] + T[2] - T[3] + T[0])
    return Fy, Fx


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    d = math.sqrt(L * L + l * l)
    T1 = np.sin(alpha + np.arctan(L / l)) * T[0]
    T2 = np.sin(alpha + np.arctan(L / l)) * T[1]
    T3 = np.sin(alpha + np.arctan(L / l)) * T[2]
    T4 = np.sin(alpha + np.arctan(L / l)) * T[3]
    torque = d * (-T2 + T1 + T3 - T4)
    a = torque / inertia
    return a


# Problem 10
def simulate_auv2_motion(
    T, alpha, L, l, mass=100, inertia=100, dt=0.1, t_final=10, x0=0, y0=0, theta0=0
):
    for i in t_final / dt:
        x = np.append(x, 1)
        print(x)


# def simulate_auv2_motion(T, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0):
print(
    calculate_auv2_angular_acceleration(np.array([10, 20, 30, 40]), 0.523599, 2, 1, 150)
)
