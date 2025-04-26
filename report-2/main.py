import numpy as np
import matplotlib.pyplot as plt
from pyfonts import load_font

def setup():
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = "CMU Serif Medium"
    plt.rc('axes', axisbelow=True)

def main():
    setup()

    specific_impulse = 400
    surface_grav_accel = 9.8
    payload_ratio_tot = 0.05
    construct_ratio = 0.1
    # Number of stages
    n = np.arange(1,11)

    delta_v_tot = n * specific_impulse * surface_grav_accel * np.log((1+construct_ratio)/(pow(payload_ratio_tot, 1/n) + construct_ratio))
    theoretical_max = specific_impulse * surface_grav_accel * (-(np.log(payload_ratio_tot))/(1 + construct_ratio))

    print(f"The theoretical limit of delta v_tot is {theoretical_max} m/s.")
    for n_i, delta_v_i in zip(n, delta_v_tot):
        print(f"For n = {n_i}, delta v_tot = {round(delta_v_i, 5)} m/s ({round(delta_v_i / theoretical_max * 100, 2)}% of theoretical limit).")

    # Scatter plot
    plt.grid(True)
    plt.scatter(n, delta_v_tot, color = 'blue', label='$\delta v_{tot}$')
    plt.xlabel('\# of stages')
    plt.ylabel('$\delta v_{total}$')
    plt.title("$\delta v_{tot}$ with different number of stages")

    # Line showing theoretical max
    plt.axhline(y=theoretical_max, color='red', linestyle='--', label=f'Theoretical Limit ({round(theoretical_max, 5)} m/s)')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

