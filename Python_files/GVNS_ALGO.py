import Methodes


# definition of four structures k = 1 -> 4
N=[Methodes.N_1,Methodes.N_2,Methodes.N_3,Methodes.N_4]

# objective function
objective_function = Methodes.fonction_objective

# number of transports
t=5

# duration of the delivery
# P=[91,71,57,37,12,13,30,26,16,55,35,20,17,3,18,59,12,16,96,7,82,10,82,75,44,54,16,45,35,28,26,80,60,6,2,31,1,47,96,85,18,2,18,92,93,55,52,68,82,98,85,54,52,92,83,7,23,35,75,77,64,50,51,33,68,7,75,68,28,71,41,5,10,50,12,28,55,36,33,26,68,77,89,71,89,6,88,19,73,38,5,54,12,2,56,44,75,49,63,9,63,80,93,70,34,87,86,6,81,59,1,30,85,22,20,41,18,42,16,89,27,78,35,12,15,19,4,4,93,60,38,36,90,95,65,52,14,54,55,17,34,51,16,62,69,52,11,73,82,75,3,12,31,51,3,36,30,21,79,17,83,17,56,44,71,79,48,68,52,37,55,69,94,92,51,88,40,67,41,85,37,29,70,64,51,5,39,25,92,81,13,76,20,10,22,45,28,47,90,89,74,79,71,23,90,74,97,56,66,51,7,83,27,13,51,41,35,5,50,95,57,50,55,52,32,85,23,3,24,2,51,67,19,65,2,85,33,13,26,64,100,41,87,54,9,50,36,20,13,98,65,14,94,32,3,37,95,70,99,31,43,57,76,70,43,36,100,49,19,2,30,94,9,88,47,70,90,48,93,28,67,12,22,35,25,47,39,3,38,71,71,24,86,46,59,19,18,49,33,59,28,20,82,76,13,92,66,20,98,99,40,9,28,32,83,21,20,100,31,74,36,50,45,30,67,52,47,49,1,7,17,69,57,95,41,29,13,5,8,7,6,43,83,92,44,84,91,92,34,10,25,23,17,82,75,46,56,7,33,12,99,67,21,25,49,8,79,82,27,64,86,87,72,5,73,88,12,86,39,80,4,81,55,41,25,95,100,82,69,27,95,44,100,67,64,18,68,17,21,49,93,52,31,96,38,92,46,21,15,33,1,38,17,33,68,1,21,65,9,36,4,13,27,66,44,65,10,56,26,4,73,65,95,37,55,91,63,97,59,39,49,74,71,97,77,3,32,25,80,53,73,56,79,80,43,44,88,64,48,32,20,96,61,42,35,3,22,75,88,26,42,34,62,3,24,9,72,78,28,87,62,34,48,68,93,60,3,69,71,88,9,21,93,6,56,12,31,87,13,36]
# P=[91,71,37,13,12,57,30,26,16]
P=[8,55,94,31,66,73,20,83,34,9,76,59,96,42,15,64,31,62,74,34,35,42,68,23,12,41,29,58,76,45,99,57,44,58,97,40,100,33,23,64,30,91,96,4,63,76,48,11,18,96,18,76,7,77,3,57,45,22,9,61,5,90,69,30,89,19,45,83,73,60,2,31,42,24,47,72,18,72,13,93,25,28,30,36,79,26,70,17,71,6,8,81,14,25,22,88,62,47,13,20,71,76,2,24,50,74,35,82,41,14,47,44,64,91,78,95,63,70,6,31,61,88,24,32,43,26,56,29,99,32,61,92,30,55,78,63,86,100,84,38,96,6,69,18,95,67,14,51,83,40,58,16,40,17,73,74,45,22,50,60,53,16,1,22,64,88,38,57,35,71,32,60,64,33,83,14,31,58,7,22,16,52,58,98,15,19,17,85,26,55,32,41,27,26,26,50,43,80,42,25,92,41,69,85,72,98,77,17,31,48,7,39,53,71,58,27,42,8,38,95,40,56,14,17,73,2,79,68,82,53,62,7,41,81,66,32,68,85,87,62,7,35,84,87,70,43,23,67,61,47,35,47,27,66,93,11,27,5,52,85,18,49,59,23,46,47,47,5,16,98,70,64,88,37,90,29,28,34,3,64,64,48,53,5,5,78,12,67,77,74,57,55,65,23,72,82,24,75,85,24,29,22,93,30,16,21,59,81,65,28,64,48,24,8,90,78,16,5,3,77,24,69,87,56,61,16,61,71,38,86,34,26,2,92,44,73,53,3,77,43,79,51,90,34,32,5,96,97,47,74,42,54,55,98,85,76,53,50,99,62,72,19,36,30,15,28,96,63,78,51,79,31,42,89,79,18,92,37,98,38,2,93,26,20,39,54,11,57,9,99,44,75,58,94,79,72,100,98,32,51,52,50,49,78,80,5,17,81,65,16,81,29,70,27,66,54,62,44,10,89,82,86,38,87,77,83,33,8,2,55,60,37,17,63,24,31,71,47,67,53,21,36,7,18,89,83,26,81,62,60,40,15,71,84,40,48,27,39,92,7,52,34,96,41,71,42,87,58,38,80,14,48,86,79,90,30,13,57,50,78,22,78,79,56,60,47,23,1,59,1,91,20,62,55,49,96,89,56,42,8,57,18,56,30,100,40,29,80,50,25,35,70,46,23,86,54,17,85,46,99,2,89,22,87,28,19,1,21,100,51,5,79,56,95,11,45,53,31,37,60,50,48,24,36,23,69,6,35,59,53,17,48,73,75,90,92,99,12,26,48,83,97,13,53,8,90,10,59,51,17,12,83,23,37,49,33,51,11,98,38,20,91,92,70,37,12,17,40,70,36,12,66,29,77,48,66,8,36,5,83,85,40,36,12,20,52,18,3,53,22,37,20,51,56,15,72,77,39,77,18,53,78,25,73,53,24,17,28,96,80,29,49,63,66,4,55,81,37,32,76,30,59,22,23,53,87,43,39,58,76,25,94,80,39,23,87,80,89,1,77,65,86,97,38,74,75,33,44,27,52,66,91,35,67,90,5,75,40,83,13,26,95,34,89,96,38,41,43,56,4,69,60,25,38,9,44,92,93,53,88,96,10,48,76,5,69,39,5,54,55,95,48,83,17,27,73,100,10,67,94,76,21,42,9,34,64,81,17,7,2,10,17,10,70,94,8,59,42,76,47,5,57,20,51,8,13,8,100,68,10,6,38,48,4,51,72,35,49,14,89,94,65,71,9,9,9,97,46,33,8,29,8,97,17,80,75,70,35,1,5,100,71,76,97,36,74,85,18,21,56,23,2,42,58,49,92,11,21,36,66,80,13,42,43,12,91,53,62,47,91,78,77,41,79,15,35,85,94,10,62,67,33,40,90,58,14,74,44,90,84,39,60,3,12,8,60,52,87,62,62,41,34,96,50,54,37,79,38,54,84,44,68,64,13,17,32,66,12,28,27,33,25,54,73,54,49,38,51,68,94,84,54,31,67,94,46,87,29,2,8,55,8,58,53,91,75,87,92,6,12,74,20,12,20,74,95,37,49,56,89,60,19,6,87,86,46,60,68,68,59,6,28,48,19,68,15,37,51,65,18,34,62,29,83,16,66,14,72,37,87,42,65,13,18,40,71,16,7,35,69,78,80,62,34,14,48,11,72,80,25,51,39,59,90,87,97,47,70,66,96,24,87,21,19,94,31,74,92,91,7,74,51,80,59,90,10,44,47,70,56,11,25,29,70,4,45,66,21,31,96,79,41,16,93,36,43,19,15,52,57]

# duration of loading the commands
# L=[2,7,10,6,4,9,9,2,9,8,2,8,2,4,6,7,6,10,8,1,7,7,9,7,9,6,8,5,5,2,7,3,1,5,3,10,7,4,4,5,6,8,4,6,5,9,10,1,10,2,8,6,5,2,2,2,7,3,4,5,7,5,2,5,8,6,2,6,3,7,4,6,7,3,3,7,10,10,10,6,3,1,10,8,6,1,9,8,1,4,3,6,9,2,1,8,2,5,1,1,1,5,10,6,2,8,7,5,2,2,1,2,9,4,2,3,5,3,6,4,4,3,10,10,10,10,3,10,10,10,8,10,3,9,4,4,3,5,1,9,2,4,10,9,8,4,3,2,4,1,5,2,6,6,1,4,5,10,3,2,4,8,10,7,1,5,7,6,9,5,3,3,4,6,7,7,4,5,2,1,10,5,1,2,3,6,8,1,10,8,1,5,3,3,10,2,2,9,3,3,3,3,10,9,2,8,2,6,5,9,5,1,10,1,10,9,6,4,8,5,7,7,3,3,5,5,6,6,1,6,6,3,1,3,8,8,8,5,10,8,5,6,2,7,2,10,9,1,10,10,2,4,9,1,6,8,8,10,1,10,6,8,1,8,6,5,7,3,9,6,1,10,3,6,8,9,6,5,5,10,5,3,8,9,7,10,1,3,3,2,1,6,8,5,9,2,6,4,9,6,4,3,5,4,5,3,5,3,7,4,9,10,5,5,8,7,1,4,10,9,9,1,4,1,7,7,7,7,7,3,6,8,9,4,6,1,8,3,9,1,6,8,8,9,3,6,5,10,1,1,6,2,3,2,3,9,5,2,5,1,3,4,10,2,9,6,6,2,7,1,10,10,9,1,5,9,2,9,8,4,10,7,1,4,6,3,5,10,8,2,3,5,8,1,2,2,3,4,5,1,10,6,2,7,4,9,9,5,6,9,9,6,7,5,7,6,7,9,6,5,4,4,5,3,10,7,6,6,9,2,4,6,3,10,7,2,10,3,4,4,3,3,10,6,4,9,9,1,3,1,10,3,9,3,6,9,10,5,1,8,7,10,1,3,5,2,2,2,7,10,8,10,2,5,10,1,1,4,8,1,8,9,7,8,2,3,9,10,10,5,1,9,3,3,7,3,8,6,7,6]
# L=[2,7,6,9,4,10,9,2,9]
L=[8,1,6,9,1,9,6,6,1,9,3,3,8,6,7,9,9,8,8,8,4,5,2,9,6,6,10,8,5,4,6,1,9,10,2,10,4,4,4,9,3,5,8,8,5,2,3,10,4,7,8,10,4,2,10,8,8,7,10,7,2,4,4,1,4,7,4,6,9,2,2,6,5,6,9,10,3,2,3,9,9,5,2,6,1,5,9,5,1,6,1,4,4,4,9,7,4,2,10,1,6,7,4,1,5,10,1,9,5,10,5,3,10,1,7,1,8,7,9,2,9,7,4,2,7,5,3,5,7,7,6,1,8,7,4,2,5,2,5,2,2,10,3,10,7,10,7,10,5,2,3,3,8,4,2,5,5,8,8,9,3,10,2,4,3,9,5,4,7,3,10,8,8,5,4,6,5,4,8,2,8,6,8,6,9,1,7,9,1,9,7,8,7,7,3,5,6,8,2,8,3,5,7,1,1,5,6,2,2,7,7,6,2,10,10,10,7,4,9,9,4,4,5,4,2,3,9,1,4,10,5,6,3,8,9,3,8,5,3,5,9,4,5,2,8,10,5,3,5,6,9,8,2,8,8,6,2,2,8,8,9,4,10,10,8,1,4,7,8,7,2,3,8,6,2,6,9,8,7,8,9,3,2,6,4,6,2,7,7,3,7,3,1,4,10,3,10,7,3,1,3,5,2,5,3,7,10,9,6,2,7,10,9,9,6,1,3,4,10,3,6,1,5,8,3,8,10,2,1,6,1,5,5,1,7,7,6,3,6,8,8,10,6,1,4,1,7,4,3,8,2,10,10,4,8,5,1,2,2,5,2,4,4,5,7,7,1,9,7,5,7,5,4,2,4,9,5,8,2,6,8,1,2,3,9,2,7,8,1,2,8,10,6,10,2,7,2,7,1,9,4,6,5,4,10,9,4,6,4,10,6,5,6,8,4,9,2,5,7,3,3,6,5,1,9,8,4,3,8,2,8,3,4,8,8,6,5,5,3,7,9,10,7,3,6,7,4,2,1,10,8,4,3,9,4,6,8,6,10,6,9,6,10,3,3,10,1,2,5,5,7,5,1,2,3,7,9,2,2,6,4,10,4,10,7,7,1,1,1,4,8,4,8,2,2,2,4,10,9,6,4,2,4,8,2,2,9,10,3,8,5,2,4,2,9,7,4,10,6,4,2,4,8,6,8,2,4,10,7,2,6,10,5,10,6,5,3,4,10,10,7,10,9,10,8,4,6,9,2,9,6,2,10,10,8,9,7,8,8,7,5,1,8,1,7,5,4,5,9,10,6,8,4,4,3,8,6,8,4,5,8,7,2,2,8,3,10,1,1,6,4,10,3,2,4,10,10,8,9,10,10,8,2,2,8,4,10,4,10,1,3,10,7,4,8,10,7,2,9,8,9,6,6,6,2,5,4,3,2,4,1,4,8,1,4,6,1,7,4,8,1,1,10,8,1,2,10,2,7,5,7,7,6,10,2,5,5,4,7,10,10,9,5,1,8,5,10,5,3,6,5,10,8,3,9,10,10,2,9,7,10,10,3,6,10,5,5,2,3,4,8,10,3,5,6,8,9,2,7,4,5,9,6,3,9,9,4,9,9,7,8,10,8,10,6,5,5,7,1,9,10,8,10,9,7,4,10,8,1,1,10,7,4,10,2,4,6,1,10,1,4,7,3,9,2,7,2,8,4,5,4,10,9,6,2,2,7,5,3,5,4,3,7,10,10,4,1,9,10,3,4,4,8,5,4,10,3,4,5,5,8,9,7,6,3,8,7,10,1,9,1,2,5,4,4,1,4,4,7,2,10,9,7,2,10,1,10,10,3,2,1,2,9,1,9,4,2,9,4,7,7,1,3,6,4,7,8,6,2,10,5,10,4,5,3,2,3,5,10,6,5,5,3,6,9,7,10,5,2,2,1,9,6,3,2,9,9,1,6,1,6,4,3,7,6,8,2,1,8,4,8,4,5,3,4,5,1,7,8,10,3,2,10,7,1,1,4,5,10,3,3,1,8,3,3,10,5,4,2,3,2,5,8,3,9,9,1,8,3,3,6,4,8,6,4,8,6,8,6,10,3,6,6,8,10,10,3,4,8,10,10,9,10,1,5,5,8,6,4,10,2,10,3,2,2,9,10,2,5,10,5,1,2,9,6,2,10,3,1,5,9,7,7,9,10,1,2,4,3,4,9,9,9,10,7,2,3,10,8,3,10,8,3,5,10,10,2,4,1,6,9,7,6,7,5,5,2,10,1,1]
# duration of delivery plus the loading for every command
R=[(x,y) for x,y in zip(L,P)]

# Generate the initiale solution using EDD rule
R.sort()
solution = R[:]
# iteration iter1, iter2 and iter3
iter1,iter2,iter3 = 0,0,0

# iteration max and nip
iter_max=500
iter_nip=5
lam = 0.5*iter_nip

# Set the first neighborhood structure for the shaking procedure to be k ← 1;
k=0

while iter1<=iter_max and iter2<=iter_nip:
    # Shaking: Generate a point π ′ at random in the N k neighborhood of π;
        # Produce a random sequence K of applying the 5 neighborhood structures;
    solution_1=N[k](solution,objective_function,t)[:]
    if objective_function(solution_1,t)<objective_function(solution,t):
        solution=solution_1[:]
        iter2=0
        iter3=0
    else:
        iter2+=1
        iter3+=1
    iter1+=iter1
    if iter3>lam and iter2<iter_nip:
        solution=Methodes.N_5(solution,objective_function,t)[:]
        iter3=0
    k=k+1
    k=k%len(N)
    print(objective_function(solution,t))

print(solution,objective_function(solution,t))





