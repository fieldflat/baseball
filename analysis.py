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

# 0: 単打
# 1: 二塁打
# 2: 三塁打
# 3: 本塁打
hitting_rate = np.array([108/(108+31+28), 31/(108+31+28), 0, 28/(108+31+28)]) # 鈴木誠也
hitting_rate = np.array([107/(107+26+40), 26/(107+26+40), 0, 40/(107+26+40)]) # 坂本勇人
# hitting_rate = np.array([62/(62+20+36), 20/(62+20+36), 0, 36/(62+20+36)]) # 村上宗隆
# hitting_rate = np.array([3089/(3089+362+96+117), 362/(3089+362+96+117), 96/(3089+362+96+117), 117/(3089+362+96+117)])  # イチロー

# 0: ランナーなし
# 1: 一塁
# 2: 二塁
# 3: 三塁
# 4: 一、二塁
# 5: 一、三塁
# 6: 二、三塁
# 7: 満塁
situation_rate = np.array([0.367, 0.307, 0.159, 0.083, 0.333, 0.421, 0.5, 0.625]) # 鈴木誠也
situation_rate = np.array([0.313, 0.292, 0.370, 0.500, 0.250, 0.438, 0.091, 0.273]) # 坂本勇人
# situation_rate = np.array([0.199, 0.298, 0.387, 0.111, 0.200, 0.333, 0.182, 0.208]) # 村上宗隆
# situation_rate = np.array([0.311, 0.316, 0.316, 0.272, 0.297, 0.318, 0.260, 0.373])  # イチロー


if __name__ == "__main__":
  iteration_count = 100000
  all_point = 0
  for _ in range(iteration_count):
    inning = 1
    out = 0
    situation = 0
    point = 0
    while inning <= 9:
      # ヒットを打つか？
      if random.random() < situation_rate[situation]:
        hit = 1
      else:
        hit = 0
      
      #
      # ヒットでないならば，アウトカウントを増やす．シチュエーションはそのまま
      #
      if hit == 0:
        out += 1
        # print('{0}アウト -----> {1}アウト'.format(out-1, out))
        if out >= 3:
          out = 0
          inning += 1
          situation = 0
          # print('========  チェンジ (次は{0}回です)  ======='.format(inning))
      
      #
      # ヒットならば...
      #
      else:
        r = random.random()
        if r < hitting_rate[0]:
          # print('単打')
          hit_type = SINGLE
        elif r < hitting_rate[0] + hitting_rate[1]:
          # print('二塁打')
          hit_type = DOUBLE
        elif r < hitting_rate[0] + hitting_rate[1] + hitting_rate[2]:
          # print('三塁打')
          hit_type = TRIPLE
        else:
          # print('本塁打')
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
      # print('シチュエーション: {0},  得点: {1}'.format(situation, point))
      # print('\n\n')
    all_point += point
  print("平均得点: {0}".format(all_point/iteration_count))
