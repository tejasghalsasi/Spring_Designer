import math   # This will import math module



D = input('Enter the Value of D: '); 
D=float(D);
F = input('Enter the Value of F: ');
F=float(F);
G = input('Enter the Value of G: ');
G=float(G);

e = input('Enter the Value of e: ');
e=float(e);

e2 = input('Enter the Value of e2: ');
e2=float(e2);

interval=float(input('Enter the Value of interval: '));


k = [0] * int(e2);

y_max =[0] * int(e2);


C = 4;
while (C<12):
    
    while (e<e2):
 
            d = D/C;
 
            K_b = (4*C + 2)/(4*C - 3);
 
            tau_s = (8*K_b*F*D*(1+e))/(3.14*math.pow(d,3));
 
            OD = D + d;
 
            ID = D - d;
    
            print("C= ",C," E= ",e," d= ",d," K_b= ",K_b," tau_s= ",tau_s," OD= ",OD," ID= ",ID);
    
            e=e+interval;
    
    
    C=C+1;


i = 3;
while (i<15):
    d = D/C;
    
    y_max[i-2] = float((8*math.pow(D, 3)*F*i)/(G*math.pow(d, 4)));

    N_t = i + 1;

    k[i-2] = F/y_max[i-2];
    
    print(" i= ",i," y_max= ",y_max[i-2]," N_t= ",N_t," k= ",k[i-2]);
    i=i+1;

	



XX=input('press enter to close this window');	