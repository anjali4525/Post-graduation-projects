#!/usr/bin/env python
# coding: utf-8

# In[2]:

[Z-Distribution]
#To import library
import scipy.stats as stat

#To take Z0 as input for Z-Distribution
Z0 = float(input("Enter tha value of Z0: "))

#To calculate the probability P(Z<Z0)
prob=stat.norm.cdf(Z0)
print('Probability(Z<Z0) is {:.6f}'.format(prob))


*****************************************************************************


#To import library
import scipy.stats as stat

#To take alpha value as input
alpha_z= float(input("Enter the value of alpha: "))

#To calculate Z0 value
Z0 = stat.norm.ppf(alpha)
print('Z0 value for the given alpha value is {:.6f}'.format(Z0))




[T-Distribution]
# To import library
import scipy.stats as stat

#To take T0 value and degree of freedom as input for T-Distribution
T0 = float(input("Enter the T0 value: "))
dof_t=float(input("Enter the degree of freedom: "))

#To Calculate the probability P(T<T0)
prob=stat.t.cdf(T0,dof_t)
print('Probability(T<T0) is {:.6f}'.format(prob))


******************************************************************************


# To import library
import scipy.stats as stat

# To take alpha value and degree of freedom 
alpha_t= float(input("Enter the value of alpha: "))
dof_t= float(input("Enter the degree of freedom: "))

# To calculating T0 value 
T0 = stat.t.ppf(alpha,dof_t)
print('T0 value for the given alpha value and the degree of freedom is  {:.6f}'.format(T0))




[Chi-square Distribution]
# To import library
import scipy.stats as stat

#To take input as critical value and degree of freedom for the Chi-square Distribution
crit_val= float(input("Enter Critical Value "))
dof_chi_sq = float(input("Enter degree of freedom "))

#To calculate the probability P(X^2 < CV)
prob=stat.chi2.cdf(crit_val,dof_chi_sq)
print('Probability(X^2 < crit_val) is {:.6f}'.format(prob))

************************************************************************************


#To import library
import scipy.stats as stat

# To take alpha value and degree of freedom as input
alpha_chi_sq= float(input("Enter alpha "))
dof_chi_sq= float(input("Enter degree of freedom "))

# To calculate critical value for the Chi_square
crit_val = stat.chi2.ppf(alpha_chi_sq,dof_chi_sq)
print('Critical value for the Chi-square is {:.6f}'.format(crit_val))


[F-Distribution]
# To import library
import scipy.stats as stat

#To take f-value and two degree of freedom for the F-Distribution
F0 = float(input("Enter the f-value "))
dof1 = float(input("Enter the first degree of freedom "))
dof2 = float(input("Enter th second degree of freedom "))

# To calculate the probability P(F<F0)
prob=stat.f.cdf(F0,dof1,dof2)
print('Probability(F<F0) is {:.6f}'.format(prob))


***************************************************************************************


# To import library
import scipy.stats as stat

# To take alpha value and two degree of freedom as input
alpha = float(input("Enter the value of alpha "))
df1 = float(input("Enter the first degree of freedom "))
df2 = float(input("Enter the second degree of freedom  "))

#To calculate F0
F0 = stat.f.ppf(alpha,df1,df2)
print('F0 value for the given alpha value and 2 degree of freedom is {:.6f}'.format(F0))







