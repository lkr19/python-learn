""""用Python设计第一个游戏"""
W=5
import random
answer=random.randint(1,100)
while W>0:
     temp = input("我心里有个数字，从1到100，你猜一猜：")
     A = int(temp)
     if A ==answer:
        print("答对，不过没有奖励")
        break
     else:
         if A > answer:
             print("大了")
         else:
             print("小了")
     W =W - 1
            
           