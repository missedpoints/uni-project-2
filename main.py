import math
import matlab
import matplotlib
e = 2.11e5 * 6895 # Convert ksi to Pa (1 ksi = 6895 Pa)
e = e * 1000 # Convert to N/m^2 (Pa)

full_length = 88 / 1000  # Convert mm to m
beam_width = 7 / 1000  # Convert mm to m
beam_depth = 8 / 1000  # Convert mm to m

moment_of_inertia = (beam_width*(beam_depth**3))/12
simple_maximum_perm_deflection = (164*(full_length**3))/48*e*moment_of_inertia
cantilever_maximum_perm_deflection = (7*242*(full_length**3))/768*e*moment_of_inertia
fixed_maximum_perm_deflection = (250*(full_length**3))/192*e*moment_of_inertia

def main():
    print("Moment of inertia: ", moment_of_inertia, "m^4")
    print("Simple maximum deflection: ", simple_maximum_perm_deflection, "m")
    print("Cantilever maximum deflection: ", cantilever_maximum_perm_deflection, "m")
    print("Fixed maximum deflection: ", fixed_maximum_perm_deflection, "m")
    print("Beam width: ", beam_width, "m")
    print("Beam depth: ", beam_depth, "m")
    print("Modulus of elasticity (E): ", e, "N/m^2")

main()