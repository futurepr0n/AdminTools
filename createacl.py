print "Here is a simple ACL Entry Creation App"

print ""

appcode = raw_input('Enter the AppCode: ')
formatted_appcode = appcode.lower()
dv = formatted_appcode + '_developer'
dl = formatted_appcode + '_devlead'



print "[" + appcode.upper() + ":/branches]"
print "@admins = rw"
print "@" + dl + " = rw"
print "@" + dv + " = rw"
print ""
print "[" + appcode.upper() + ":/tags]"
print "@admins = rw"
print "@" + dl + " = rw"
print "@" + dv + " = r"
print ""
print "[" + appcode.upper() + ":/trunk]"
print "@admins = rw"
print "@" + dl + " = rw"
print "@" + dv + " = r"
print ""
print "[" + appcode.upper() + ":/]"
print "@admins = rw"
print "@" + dl + " = r"
print "@" + dv + " = r"

print ""

print(dl)
print(dv)

