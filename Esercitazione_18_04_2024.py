# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:01:52 2024

@author: lpers
"""
# import numpy as np
# import matplotlib.pyplot as plt
# t=np.linspace(0,10,10000)
# V=3*np.exp(-t/3)*np.sin(np.pi*t)
# V1=V[V>0]
# t1=t[V>0]
# plt.plot(t1,V1)
# t2=t[V<=0]
# V2=np.zeros(len(t2))
# plt.scatter(t2,V2)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# t=np.linspace(0,10,10000)
# V=3*np.exp(-t/3)*np.sin(np.pi*t)
# V2=np.where(V>0, V,0)
# plt.plot(t,V2)

# import numpy as np
# import matplotlib.pyplot as plt
# t=np.linspace(0,10,10000)
# V=3*np.exp(-t/3)*np.sin(np.pi*t)
# for i in range(len(V)):
#     if V[i]>0:
#         V1=V[i]
#     else:
#         V1=0
# plt.plot(t,V2)

import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,10,1000)
V=3*np.exp(-t/3)*np.sin(np.pi*t)
for i in range(len(V)):
    if V[i]>0:
        plt.scatter(t[i],V[i])
    else:
        plt.scatter(t[i],0)
