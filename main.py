import math
import matlab
import matplotlib
# i = moment of intertia. FIND MOMENT OF INERTIA!
e = 2.11e5  # in ksi ## Young's Modulus for Carbon Steel.

#####################
full_length = 88  # length of bar
beam_width = 7  # these are recorded in millimeters.
beam_depth = 8  # depth of bar.
#####################

moment_of_inertia = (beam_width * (beam_depth**3))/12

simply_maximum_deflection = 164

simple_moment_of_inertia = (beam_width*(beam_depth**3))/12

simple_maximum_perm_deflection = (
    164*(full_length**3))/48*e*simple_moment_of_inertia


def main():
    print("Permenant deflection is.. ", simple_maximum_perm_deflection)
    print("Simple moment of inertia..", simple_moment_of_inertia, "mm^4")
    print(beam_depth, beam_depth)
    print(e)


main()
