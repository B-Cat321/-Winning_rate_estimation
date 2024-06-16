import math

# 入力される値を整理
score = int(input())
lose_score = int(input())

score_average = int(input())
lose_score_average = int(input())

game_count = int(input())

# イニング当たりの平均得点、平均失点（Palmer-RPWに使う）
average_score_per_inning = score_average / 9
average_lose_score_per_inning = lose_score_average / 9

# リーグの得点数、リーグのイニング数（Tango-RPWに使う）
league_score = int(input())
league_inning = int(input())

# 平均得点と平均失点の差の絶対値（Tango-RPW-RDに使う）
score_difference = abs(score_average - lose_score_average)

# Run Per Game（RPG）の計算
rpg = (score + lose_score) / game_count

def Cook(score, lose_score):
    # 勝率の計算
    winning_rate = 0.484 * (score + lose_score)
    return winning_rate

def Soolman(score_average, lose_score_average):
    # 勝率の計算
    winning_rate = (0.102 * score_average) -  (0.103 * lose_score_average) + 0.505
    return winning_rate

def James_2(score, lose_score):
    # 勝率の計算
    winning_rate = score ** 2 / (score ** 2 + lose_score ** 2)
    return winning_rate

def James_183(score, lose_score):
    # 勝率の計算
    winning_rate = score ** 1.83 / (score ** 1.83 + lose_score ** 1.83)
    return winning_rate

def Pythagenport(score, lose_score, rpg):
    # 勝率の計算
    
    multiplier = 1.50 * math.log(rpg) + 0.45
    winning_rate = score ** multiplier / (score ** multiplier + lose_score ** multiplier)
    return winning_rate

def Pythagenpat(score, lose_score, rpg):
    # 勝率の計算
    multiplier = rpg ** 0.28
    winning_rate = score ** multiplier / (score ** multiplier + lose_score ** multiplier)
    return winning_rate

def Palmer_RPW(average_score_per_inning, average_lose_score_per_inning):
    # 勝率の計算
    winning_rate = 10 *  math.sqrt(average_score_per_inning + average_lose_score_per_inning)
    return winning_rate

def Tango_RPW(rpg):
    # 勝率の計算
    winning_rate = (0.75 * rpg) / 3
    return winning_rate

def Tango_RPW_RD(rpg, score_difference):
    # 勝率の計算
    winning_rate = (0.8 * rpg) + 0.4 * score_difference + 3  
    return winning_rate