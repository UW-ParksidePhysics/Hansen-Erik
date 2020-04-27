%Code taken from Houcque2005_5-ControlFlowAndOperators_
%IntroductionToMATLABForEngineeringStudents.pdf and updated by Erik Hansen
a = input('Input a')
b = input('Input b')
c = input('Input c')
discr = b*b - 4*a*c
Root1= (-b + sqrt(discr))/(2*a)
Root2= (-b - sqrt(discr))/(2*a)
if discr < 0
    disp('Warning: discriminant is negative, roots are imaginary');
elseif discr == 0
    disp('Discriminant is zero, roots are repeated')
else 
    disp('Roots are real')
end
    