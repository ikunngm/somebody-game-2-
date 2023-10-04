import random
from signal import CTRL_BREAK_EVENT, CTRL_C_EVENT 
from settings import*
from main import*
from mjj import*
print ('恶魔之城？黑气笼罩，似乎是个不吉之地......')  
print('魔王奴役着人民，他们需要你！')
print('别害怕,坤坤会用唱跳Rap和篮球助你一臂之力!')
print('出发吧,圣骑士!')
# 游戏循环
while True:    
    while True:
        # 金币随机增加
        coin += random.randint(coin_scopes[0], coin_scopes[1])
        # 减少道具冷却
        if basketball_time > 0:
            basketball_time -= 1
        else:
            basketball_time = 0 
        if ctr_time > 0:
            ctr_time -= 1
        else:
            ctr_time = 0 
        # 随机暴击
        crit = random.randint(1, int(1/crit_rate))
        if crit == 1:
            king_xp -= 2 * attack    
        # 控制 
        if crit == 1: 
           print('暴击!')
           print('魔王血量还有' + str(king_xp),  '你的血量还有'+ str(you_xp),'，暴击伤害，金币剩余' + str(coin), '/攻击(Enter)/进入商店(B)/使用道具(I)/尝逝逃跑(X)')   
        if crit != 1:
           print('魔王血量还有' + str(king_xp), '你的血量还有'+ str(you_xp),'，伤害为'+ str(attack), '，金币剩余' + str(coin), '/攻击(Enter)/进入商店(B)/使用道具(I)/尝逝逃跑(X)') 
        put = input()
        # 攻击
        if put == '':
            king_xp -= attack
            if crit == 1:
             king_xp -= attack 
        #伤害
        if king_xp<=1000 and put =='':    
        #随机伤害    
            jj = random.randint(1, int(1/jj_rate))
            if jj == 1:
               you_xp -= hurt    
        # 商店
        elif put == 'B' or put == 'b':
            while True:
                print('商店，金币剩余' + str(coin))
                print(basketball, '/购买(1)')
                print(ctr,'/购买(2)')
                print('选择你要购买的商品吧/离开商店(X)')
                put_shop = input()
                if put_shop == '1':
                    if basketball_state == 0:
                        if coin >= 1000:
                            coin -= 1000
                            basketball_state += 1
                            print('购买成功')
                        else:
                            print('你是想白嫖吗?')
                    else:
                        print('做人不要太贪心')
                if put_shop == '2':
                    if ctr_state == 0   :
                        if coin >=1500:
                            coin -= 1500
                            ctr_state += 1
                            print('购买成功')
                        else:
                            print('你是想白嫖吗?')
                    else:
                        print('做人不要太贪心')
                elif put_shop == 'X' or put_shop == 'x':
                    print('离开商店')
                    break
        #彩蛋
        if coin == 114514:
            print('忆一时，悟一世？这不对吧？')
            coin -= 114514
        #技能
        elif put == 'I' or put == 'i':
            while True:
                if basketball_state == 0 and ctr_state == 0:
                   print('你是想白嫖吗?你还没有买技能呢/退出(X)')
                if basketball_state == 1 or ctr_state == 1:
                    print(basketball, '冷却剩余(' + str(basketball_time), ')/发动(1)')
                    print(ctr,'冷却剩余(' + str(ctr_time), ')/发动(2)')
                    print('选择你要使用的道具吧/取消使用(X)')
                put_prop = input()
                # 篮球
                if put_prop == '1':
                    if basketball_time == 0 and basketball_state == 1: 
                        # 道具'篮球'（-50）
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        basketball_time = 5
                    else:
                        print('再等等吧')
                elif put_prop == 'X' or put_prop == 'x':
                 print('取消使用')
                 break
                #唱跳RAP
                if put_prop == '2':
                    if ctr_time == 0 and ctr_state == 1:
                        # 道具'唱跳Rap'（-105）
                        print(str(king_xp) + '-5')
                        king_xp -= 5
                        print(str(king_xp) + '-10')
                        king_xp -= 10
                        print(str(king_xp) + '-15')
                        king_xp -= 15
                        print(str(king_xp) + '-20')
                        king_xp -= 20
                        print(str(king_xp) + '-25')
                        king_xp -= 25
                        print(str(king_xp) + '-30')
                        king_xp -= 30
                        ctr_time = 15
                    else:
                        print('再等等吧')
                elif put_prop == 'X' or put_prop == 'x':
                    print('取消使用')
                    break    
         # 逃跑
        elif put == 'X' or put == 'x':
            print('胆小鬼，你逃离了恶魔之城，你连攻击都不会吗?真的太逊了')
            break
         #你死了
        if you_xp <= 0: 
             print('你死了')
             break
         # 战胜
        if king_xp <= 0:
             print('英雄，你战胜了魔王!!!')
             break
    print('任意键继续玩/退出(X)')
    put_exit = input()
    if put_exit == 'X' or put_exit == 'x':
        break