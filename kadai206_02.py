import collections

x = "たったひとつのしんじつみぬく、みためはこども、ずのうはおとな"
print(x)
l = list(x)
c = collections.Counter(l)

for key, value in c.items():
    print(key + ":" + str(value) + "個")
