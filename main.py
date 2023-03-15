import math
import matlab
import matplotlib
##i = moment of intertia. FIND MOMENT OF INERTIA!
e = 2.11e5 ## in ksi ## Young's Modulus for Carbon Steel.

##################
full_length = 88## length of bar
beam_width = 7#### these are recorded in millimeters.
beam_depth = 8**3#### depth of bar.
##################
simple_i = (beam_width * (beam_depth))/12
cantilever_i = 0 ## TODO: Cantilever's moment of inertia.
fixed_i = 0 ##TODO: Fixed beam's moment of inertia.

simply_maximum_deflection = 164

simple_moment_of_inertia = (beam_width*(beam_depth))/12

simple_maximum_perm_deflection = (164*(full_length**3))/48*e*simple_moment_of_inertia

def main():
    print("Permenant deflection is.. ",simple_maximum_perm_deflection)
    print("Simple moment of inertia..",simple_moment_of_inertia)
    print(beam_depth,beam_depth**-3)
    print(e)

main()