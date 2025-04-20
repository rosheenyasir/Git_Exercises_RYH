[33mcommit b6fd9edcecad84d37e52e93a9acbd02233163316[m
Author: Aku Niskanen <aku.niskanen@tuni.fi>
Date:   Mon Oct 21 01:47:04 2019 -0700

    Strings to integers

[1mdiff --git a/basics/mergesort.py b/basics/mergesort.py[m
[1mindex 54c4078..468ba8b 100644[m
[1m--- a/basics/mergesort.py[m
[1m+++ b/basics/mergesort.py[m
[36m@@ -11,6 +11,15 @@[m [mdef debug_print(debug_msg=None, **kwargs):[m
 if __name__ == "__main__":[m
     input_str = input("Enter numbers, separated by ',': ")[m
 [m
[31m-    unsorted_list = input_str.split(",")[m
[32m+[m[32m    input_list = input_str.split(",")[m
[32m+[m[32m    debug_print(input_list=input_list)[m
 [m
[31m-    debug_print(unsorted_list=unsorted_list)[m
[32m+[m[32m    value_list = [][m
[32m+[m[32m    for x in input_list:[m
[32m+[m[32m        try:[m
[32m+[m[32m            value_list.append(int(x))[m
[32m+[m[32m        except ValueError as err:[m
[32m+[m[32m            print("Invalid input.")[m
[32m+[m[32m            quit(1)[m
[32m+[m
[32m+[m[32m    debug_print(value_list=value_list)[m
