L=[3, 4]
L1 = [1, 2, L]
L2 = L1.copy()
L2[2][0]=0

print("normal copy: ")
print("L1 = ", L1)
print("L2 = ", L2)

import copy
L=[3, 4]
L1 = [1, 2, L]
L2 = copy.deepcopy(L1)
L2[2][0]=0

print("deep copy: ")
print("L1 = ", L1)
print("L2 = ", L2)
