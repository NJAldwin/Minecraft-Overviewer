import sys

sys.path.append(".")

from overviewer_core.nbt import load

print "Inspecting %s" % sys.argv[1]

data  = load(sys.argv[1])[1]


print "Position:  %r" % data['Pos']
print "Health:    %s" % data['Health']
print "Inventory: %d items" % len(data['Inventory'])
for item in data['Inventory']:
    print "      %r" % item
