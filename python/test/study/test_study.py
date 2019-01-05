import os
import sys
import datetime
import time
import string


todayCDC = 6596
yesterdayCDC = 6595
old_todayCDC = "%todayCDC"
old_yesterdayCDC = "%yesterdayCDC"

with open("/root/Test/123.txt","r") as file_name:
    for i in file_name:
        if old_todayCDC in i:
            i = i.replace(old_todayCDC, str(todayCDC))
            # if
            print(i, end="")
            try:
                # os.stat('%s%s' % ("/root/Test/", i))
                if os.path.exists('%s%s' % ("/root/Test/", i)):
                    print(i, end="")
                else:
                    print(os.path.exists('%s%s' % ("/root/Test/", i)))

            except IOError:
                print("1")
        # else:
        #     i = i.replace(old_yesterdayCDC, str(yesterdayCDC))
        #     print(i, end="")
