from leavenew import Leave
from basketnew import BasketOfLeave
from restrictnew import RestrictedLeave
r1=RestrictedLeave(22790,"sai",20,"2001-06-14")
print(r1.display_dob())
b1=BasketOfLeave(22790,"sai",20,1)
print(b1.display())
print(b1.display())
l1=Leave(22772,"gowthami", 20)