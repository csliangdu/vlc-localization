
origin = 'center'

w = 28.0
l = 29.0

#position_of_transmitters = [-w/2*2.54 l/2*2.54 0; w/2*2.54 l/2*2.54 0; w/2*2.54 -l/2*2.54 0; -w/2*2.54 -l/2*2.54 0; 0 0 0];
#frequency_of_transmitter = [2000; 2500; 3000; 3500; 4000];
transmitters = {
        2000 : ((-13.25*2.54, 11.25*2.54, 0),),
        2500 : ((-2*2.54, -2*2.54, 0),),
        3000 : ((11.25*2.54, -13.5*2.54, 0),),
        3500 : ((-12.75*2.54, -13.5*2.54, 0),),
        4000 : ((13*2.54, 13.5*2.54, 0),),
        }