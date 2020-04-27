%Code taken from Houcque2005_5-ControlFlowAndOperators_
%IntroductionToMATLABForEngineeringStudents.pdf, MatLab Online Help, and updated by Erik Hansen
a = nchoosek(1:1000,2);
c = sqrt(sum(a.^2,2)); 
f = c == fix(c) & c <= 1000;
PythgoreanIntegerTriplets = [a(f,:) c(f)]
fileID=fopen('PythagoreanIntegerTriplets.txt','wt');
fprintf(fileID,'Triplets');
fclose(fileID);
