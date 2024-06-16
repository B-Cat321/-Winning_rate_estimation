import math
import streamlit as st
import pandas as pd

# Streamlitでの入力
st.title("勝率推定式の一覧")
score: int = st.number_input("得点", min_value=1, value=1, step=1)
lose_score: int = st.number_input("失点", min_value=1, value=1, step=1)
score_average: float = st.number_input("平均得点", min_value=0.01, value=1.0)
lose_score_average: float = st.number_input("平均失点", min_value=0.01, value=1.0)
game_count: int = st.number_input("試合数", min_value=1, value=1, step=1)

# 計算
average_score_per_inning: float = score_average / 9
average_lose_score_per_inning: float = lose_score_average / 9
score_difference: float = abs(score_average - lose_score_average)
rpg: float = (score + lose_score) / game_count

def Cook(score: int, lose_score: int) -> float:
    return 0.484 * (score / lose_score)

def Soolman(score_average: float, lose_score_average: float) -> float:
    return (0.102 * score_average) -  (0.103 * lose_score_average) + 0.505

def James_2(score: int, lose_score: int) -> float:
    return score ** 2 / (score ** 2 + lose_score ** 2)

def James_183(score: int, lose_score: int) -> float:
    return score ** 1.83 / (score ** 1.83 + lose_score ** 1.83)

def Pythagenport(score: int, lose_score: int, rpg: float) -> float:
    multiplier: float = 1.50 * math.log(rpg) + 0.45
    return score ** multiplier / (score ** multiplier + lose_score ** multiplier)

def Pythagenpat(score: int, lose_score: int, rpg: float) -> float:
    multiplier: float = rpg ** 0.28
    return score ** multiplier / (score ** multiplier + lose_score ** multiplier)

def Palmer_RPW(average_score_per_inning: float, average_lose_score_per_inning: float) -> float:
    return 10 *  math.sqrt(average_score_per_inning + average_lose_score_per_inning)

def Tango_RPW(rpg: float) -> float:
    return (0.75 * rpg) + 3

def Tango_RPW_RD(rpg: float, score_difference: float) -> float:
    return (0.8 * rpg) + 0.4 * score_difference + 3

# 勝率の計算
results: dict[str, list[str | float]] = {
    "Method": ["Cook", "Soolman", "James_2", "James_183", "Pythagenport", "Pythagenpat", "Palmer_RPW", "Tango_RPW", "Tango_RPW_RD"],
    "Winning Rate": [
        Cook(score, lose_score),
        Soolman(score_average, lose_score_average),
        James_2(score, lose_score),
        James_183(score, lose_score),
        Pythagenport(score, lose_score, rpg),
        Pythagenpat(score, lose_score, rpg),
        Palmer_RPW(average_score_per_inning, average_lose_score_per_inning),
        Tango_RPW(rpg),
        Tango_RPW_RD(rpg, score_difference)
    ]
}

# 結果をデータフレームに変換
df: pd.DataFrame = pd.DataFrame(results)

# テーブルとして表示
st.table(df)