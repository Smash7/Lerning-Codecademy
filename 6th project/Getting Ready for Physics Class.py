train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
# 1
def f_to_c(f_temp: float) -> float:
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# 3
def c_to_f(c_temp: float) -> float:
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


# 5
def get_force(mass: float, acceleration: float) -> float:
    return mass * acceleration


# 8
def get_energy(mass) -> float:
    c = 3*10**8
    return mass ** c


# 11
def get_work(mass: float, acceleration: float, distance: float) -> float:
    return get_force(mass, acceleration) * distance


# 2
f100_in_celsius = f_to_c(100)

# 4
c0_in_fahrenheit = c_to_f(0)

# 6
train_force = get_force(train_mass, train_acceleration)

# 7
print(f"“The GE train supplies {train_force} Newtons of force.”")

# 9
bomb_energy = get_energy(bomb_mass)

# 10
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# 12
train_work = get_work(train_mass, train_acceleration, train_distance)

# 13
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
