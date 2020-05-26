import numpy as np
import random

#
# HIT_TYPE
#
SINGLE = 0
DOUBLE = 1
TRIPLE = 2
HOMERUN = 3

#
# SITUATION
#
NO_RUNNER = 0
FIRST = 1
SECOND = 2
THIRD = 3
FIRST_SECOND = 4
FIRST_THIRD = 5
SECOND_THIRD = 6
FULL_BASE = 7

#
# SITUATION_NAME
#
SITUATION_NAME = ['走者なし', '走者一塁', '走者二塁', '走者三塁', '走者一、二塁', '走者一、三塁', '走者二、三塁', '走者満塁']

#
# RESULT
#
OUT = 0
HIT = 1
FOUR_DEAD_BALLS = 2

# 0: 単打
# 1: 二塁打
# 2: 三塁打
# 3: 本塁打
# hitting_rate = np.array([107/(107+26+40), 26/(107+26+40), 0, 40/(107+26+40)]) # 坂本勇人
# hitting_rate = np.array([62/(62+20+36), 20/(62+20+36), 0, 36/(62+20+36)]) # 村上宗隆
# hitting_rate = np.array([3089/(3089+362+96+117), 362/(3089+362+96+117), 96/(3089+362+96+117), 117/(3089+362+96+117)])  # イチロー
# hitting_rate = np.array([71/(71+20+43), 20/(71+20+43), 0, 43/(71+20+43)]) # 山川穂高
# hitting_rate = np.array([103/(103+24+2+29), 24/(103+24+2+29), 2/(103+24+2+29), 29/(103+24+2+29)]) # 吉田正尚
# hitting_rate = np.array([103/(103+34+2+23), 34/(103+34+2+23), 2/(103+34+2+23), 23/(103+34+2+23)]) # 森友哉


# 0: ランナーなし
# 1: 一塁
# 2: 二塁
# 3: 三塁
# 4: 一、二塁
# 5: 一、三塁
# 6: 二、三塁
# 7: 満塁

# 鈴木誠也 (8.95496)
player_name = "鈴木誠也"
get_on_by_hit = 167/612 # 安打数/打席数
get_on_by_others = 110/612 # 四死球数/打席数
hitting_rate = np.array([108/(108+31+28), 31/(108+31+28), 0, 28/(108+31+28)])

# 山田哲人 (7.26743)
player_name = "山田哲人"
get_on_by_hit = 141/641  # 安打数/打席数
get_on_by_others = 116/641  # 四死球数/打席数
hitting_rate = np.array([66/(141), 35/(141), 5/(141), 35/(141)])

# 坂本勇人 (7.24442)
player_name = "坂本勇人"
get_on_by_hit = 173/639  # 安打数/打席数
get_on_by_others = 79/639  # 四死球数/打席数
hitting_rate = np.array([107/(107+26+40), 26/(107+26+40), 0, 40/(107+26+40)])

# 筒香嘉智 (6.4414)
player_name = "筒香嘉智"
get_on_by_hit = 126/557  # 安打数/打席数
get_on_by_others = 90/557  # 四死球数/打席数
hitting_rate = np.array([73/(126), 24/(126), 0, 29/(126)])

# バレンティン (6.3496)
player_name = "バレンティン"
get_on_by_hit = 115/468  # 安打数/打席数
get_on_by_others = 55/468  # 四死球数/打席数
hitting_rate = np.array([69/(115), 13/(115), 0, 29/(115)])

# 丸佳浩 (6.20968)
player_name = "丸佳浩"
get_on_by_hit = 156/631  # 安打数/打席数
get_on_by_others = 89/631  # 四死球数/打席数
hitting_rate = np.array([102/(156), 26/(156), 1/156, 27/(156)])

# ソト (6.10045)
player_name = "ソト"
get_on_by_hit = 139/584  # 安打数/打席数
get_on_by_others = 64/584  # 四死球数/打席数
hitting_rate = np.array([78/(139), 18/(139), 0/139, 43/(139)])

# ビシエド (5.83177)
# player_name = "ビシエド"
# get_on_by_hit = 168/594  # 安打数/打席数
# get_on_by_others = 54/594  # 四死球数/打席数
# hitting_rate = np.array([107/(168), 43/(168), 0, 18/(168)])

# 糸井嘉男
# player_name = "糸井嘉男"
# get_on_by_hit = 120/444  # 安打数/打席数
# get_on_by_others = 59/444  # 四死球数/打席数

# イチロー (5.04846)
# player_name = "イチロー"
# get_on_by_hit = 4367/14832
# get_on_by_others = 1145/14832
# hitting_rate = np.array([(4367-573-119-235)/(4367), 573/(4367), 119/(4367), 235/(4367)])


#
# メイン関数
#
if __name__ == "__main__":
  GAME_COUNT = 100000
  all_point = 0
  hit_count = 0
  four_dead_balls_count = 0
  DISPLAY = 0
  for _ in range(GAME_COUNT):
    inning = 1
    out = 0
    situation = 0
    point = 0
    while inning <= 9:
      # ヒットを打つか？
      r = random.random()
      if r < get_on_by_hit:
        hit = HIT
        hit_count += 1
      elif r < get_on_by_hit + get_on_by_others:
        print('四死球') if DISPLAY == 1 else None
        hit = FOUR_DEAD_BALLS
        four_dead_balls_count += 1
      else:
        print('OUT!') if DISPLAY == 1 else None
        hit = OUT
      
      #
      # 凡打の場合
      #
      if hit == OUT:
        #
        # ランナーなし
        #
        if (situation == NO_RUNNER):
          out += 1
          situation = NO_RUNNER

        #
        # 一塁
        #
        elif (situation == FIRST):
          r = random.random()
          if r < 1/3:
            out += 1
            situation = FIRST
          elif r < 2/3:
            out += 1
            situation = SECOND
          else:
            out += 2
            situation = NO_RUNNER


        #
        # 二塁
        #
        elif (situation == SECOND):
          r = random.random()
          if r < 1/2:
            out += 1
            situation = THIRD
          else:
            out += 1
            situation = SECOND

        #
        # 三塁
        #
        elif (situation == THIRD):
          r = random.random()
          if r < 1/2:
            out += 1
            situation = THIRD
          else:
            out += 1
            situation = NO_RUNNER
            if out <= 2:
              point += 1

        #
        # 一、二塁
        #
        elif (situation == FIRST_SECOND):
          r = random.random()
          if r < 1/3:
            out += 1
            situation = FIRST_SECOND
          elif r < 2/3:
            out += 1
            situation = SECOND_THIRD
          else:
            out += 2
            situation = THIRD

        #
        # 一、三塁
        #
        elif (situation == FIRST_THIRD):
          r = random.random()
          if r < 1/4:
            out += 1
            situation = FIRST_SECOND
          elif r < 2/4:
            out += 2
            situation = NO_RUNNER
            if out <= 2:
              point += 1
          elif r < 3/4:
            out += 1
            situation = FIRST
            if out <= 2:
              point += 1
          else:
            out += 1
            situation = SECOND
            if out <= 2:
              point += 1


        #
        # 二、三塁
        #
        elif (situation == SECOND_THIRD):
          r = random.random()
          if r < 1/3:
            out += 1
            situation = SECOND_THIRD
          elif r < 2/3:
            out += 1
            situation = FIRST_THIRD
          else:
            out += 1
            situation = THIRD
            if out <= 2:
              point += 1

        #
        # 満塁
        #
        elif (situation == FULL_BASE):
          r = random.random()
          if r < 1/3:
            out += 1
            situation = FULL_BASE
          elif r < 2/3:
            out += 1
            situation = SECOND_THIRD
            if out <= 2:
              point += 1
          else:
            out += 2
            situation = SECOND_THIRD
      
      #
      # ヒットならば...
      #
      elif hit == HIT:
        r = random.random()
        if r < hitting_rate[0]:
          print('*=*=*=*= 単打 *=*=*=*=') if DISPLAY == 1 else None
          hit_type = SINGLE
        elif r < hitting_rate[0] + hitting_rate[1]:
          print('*=*=*=*= 二塁打 *=*=*=*=') if DISPLAY == 1 else None
          hit_type = DOUBLE
        elif r < hitting_rate[0] + hitting_rate[1] + hitting_rate[2]:
          print('*=*=*=*= 三塁打 *=*=*=*=') if DISPLAY == 1 else None
          hit_type = TRIPLE
        else:
          print('*=*=*=*= 本塁打 *=*=*=*=') if DISPLAY == 1 else None
          hit_type = HOMERUN
        
        # hit_typeに応じて，situationを変更する．

        #
        # ランナーなし
        #
        if (situation == NO_RUNNER):
          if (hit_type == SINGLE):
            situation = FIRST
          elif (hit_type == DOUBLE):
            situation = SECOND
          elif (hit_type == TRIPLE):
            situation = THIRD
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 1
        
        #
        # 一塁
        #
        elif (situation == FIRST):
          if (hit_type == SINGLE):
            if random.random() < 0.5:
              situation = FIRST_SECOND
            else:
              situation = FIRST_THIRD
          elif (hit_type == DOUBLE):
            situation = SECOND_THIRD
          elif (hit_type == TRIPLE):
            situation = TRIPLE
            point += 1
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 2
        
        #
        # 二塁
        #
        elif (situation == SECOND):
          if (hit_type == SINGLE):
            if random.random() < 0.5:
              situation = FIRST_THIRD
            else:
              situation = FIRST
              point += 1
          elif (hit_type == DOUBLE):
            situation = SECOND
            point += 1
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 1
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 2
        
        #
        # 三塁
        #
        elif (situation == THIRD):
          if (hit_type == SINGLE):
            situation = FIRST
            point += 1
          elif (hit_type == DOUBLE):
            situation = SECOND
            point += 1
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 1
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 2
        
        #
        # 一、二塁
        #
        elif (situation == FIRST_SECOND):
          if (hit_type == SINGLE):
            if random.random() < 0.5:
              situation = FULL_BASE
            else:
              situation = FIRST_SECOND
              point += 1
          elif (hit_type == DOUBLE):
            if random.random() < 0.5:
              situation = SECOND_THIRD
              point += 1
            else:
              situation = SECOND
              point += 2
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 2
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 3
        
        #
        # 一、三塁
        #
        elif (situation == FIRST_THIRD):
          if (hit_type == SINGLE):
            situation = FIRST_SECOND
            point += 1
          elif (hit_type == DOUBLE):
            if random.random() < 0.5:
              situation = SECOND_THIRD
              point += 1
            else:
              situation = SECOND
              point += 2
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 2
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 3
        
        #
        # 二、三塁
        #
        elif (situation == SECOND_THIRD):
          if (hit_type == SINGLE):
            if random.random() < 0.5:
              situation = FIRST_THIRD
              point += 1
            else:
              situation = FIRST
              point += 2
          elif (hit_type == DOUBLE):
            situation = SECOND
            point += 2
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 2
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 3
        
        #
        # 満塁
        #
        elif (situation == FULL_BASE):
          if (hit_type == SINGLE):
            if random.random() < 0.5:
              situation = FULL_BASE
              point += 1
            else:
              situation = FIRST_SECOND
              point += 2
          elif (hit_type == DOUBLE):
            if random.random() < 0.5:
              situation = SECOND_THIRD
              point += 2
            else:
              situation = SECOND
              point += 3
          elif (hit_type == TRIPLE):
            situation = THIRD
            point += 3
          elif (hit_type == HOMERUN):
            situation = NO_RUNNER
            point += 4
      
      #
      # 四死球の場合
      #
      elif hit == FOUR_DEAD_BALLS:
        #
        # ランナーなし
        #
        if (situation == NO_RUNNER):
          situation = FIRST

        #
        # 一塁
        #
        elif (situation == FIRST):
          situation = FIRST_SECOND

        #
        # 二塁
        #
        elif (situation == SECOND):
          situation = FIRST_SECOND

        #
        # 三塁
        #
        elif (situation == THIRD):
          situation = FIRST_THIRD

        #
        # 一、二塁
        #
        elif (situation == FIRST_SECOND):
          situation = FULL_BASE

        #
        # 一、三塁
        #
        elif (situation == FIRST_THIRD):
          situation = FULL_BASE

        #
        # 二、三塁
        #
        elif (situation == SECOND_THIRD):
          situation = FULL_BASE

        #
        # 満塁
        #
        elif (situation == FULL_BASE):
          situation = FULL_BASE
          point += 1
      print('{0}アウト,   シチュエーション: {1},  得点: {2}'.format(out, SITUATION_NAME[situation], point)) if DISPLAY == 1 else None

      #
      # 3アウトかどうか？
      #
      if out >= 3:
        out = 0
        inning += 1
        situation = NO_RUNNER
        print('==== 次は{0}回です ====\n\n'.format(inning)) if DISPLAY == 1 else None
    all_point += point
  print('選手名: {0}'.format(player_name))
  print("平均得点: {0}".format(all_point/GAME_COUNT))
  print('平均安打数: {0},  平均四死球数: {1}'.format(hit_count/GAME_COUNT, four_dead_balls_count/GAME_COUNT))
