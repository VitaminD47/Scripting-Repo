eigrp, ospf, rip = 90, 110, 120
path1,path2,path3 = 3, 6, 9
admin_distance = (eigrp * path1)+ (ospf * path2) + (rip * path3)
print(admin_distance)
