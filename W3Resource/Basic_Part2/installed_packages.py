import pkg_resources
count = 0
installed_packages = pkg_resources.working_set

# installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
installed_packages_list = []
for i in installed_packages:
    count += 1
    installed_packages_list.append(["%s==%s" % (i.key, i.version)])
    

for m in installed_packages_list:
    print(m)