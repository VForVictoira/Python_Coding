# coding=utf-8
while 1 :
    words = input("谁是这个世界上最美的女生？")
    if words == "林嘉婷" :
       print("真聪明~")
       while 1:
           answer = input("你喜欢她吗？")
           if answer== "喜欢":
                 print("她说她也喜欢你哦~")
                 break
           else:
                 print("我再问你一遍！")
                 continue
       break
    else:
       continue
