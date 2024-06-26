import math
import streamlit as st
import pandas as pd

# Streamlitでの入力
st.title("勝率推定式の一覧")
runs: int = st.number_input("得点", min_value=1, value=1, step=1)
runs_allowed: int = st.number_input("失点", min_value=1, value=1, step=1)
game_count: int = st.number_input("試合数", min_value=1, value=1, step=1)

# 計算
runs_average: float = runs / game_count
runs_allowed_average: float = runs_allowed / game_count
average_runs_per_inning: float = runs_average / 9
average_runs_allowed_per_inning: float = runs_allowed_average / 9
runs_difference: float = abs(runs_average - runs_allowed_average)
runs_per_game: float = (runs + runs_allowed) / game_count

def Cook(runs: int, runs_allowed: int) -> float:
    return 0.484 * (runs / runs_allowed)

def Soolman(runs_average: float, runs_allowed_average: float) -> float:
    return (0.102 * runs_average) -  (0.103 * runs_allowed_average) + 0.505

def James_2(runs: int, runs_allowed: int) -> float:
    return runs ** 2 / (runs ** 2 + runs_allowed ** 2)

def James_183(runs: int, runs_allowed: int) -> float:
    return runs ** 1.83 / (runs ** 1.83 + runs_allowed ** 1.83)

def Pythagenport(runs: int, runs_allowed: int, runs_per_game: float) -> float:
    multiplier: float = 1.50 * math.log(runs_per_game) + 0.45
    return runs ** multiplier / (runs ** multiplier + runs_allowed ** multiplier)

def Pythagenpat(runs: int, runs_allowed: int, runs_per_game: float) -> float:
    multiplier: float = runs_per_game ** 0.28
    return runs ** multiplier / (runs ** multiplier + runs_allowed ** multiplier)

def Palmer_RPW(average_runs_per_inning: float, average_runs_allowed_per_inning: float) -> float:
    return 10 *  math.sqrt(average_runs_per_inning + average_runs_allowed_per_inning)

def Tango_RPW(runs_per_game: float) -> float:
    return (0.75 * runs_per_game) + 3

def Tango_RPW_RD(runs_per_game: float, runs_difference: float) -> float:
    return (0.8 * runs_per_game) + 0.4 * runs_difference + 3

# 勝率の計算
results: dict[str, list[str | float]] = {
    "Method": ["Cook", "Soolman", "James_2", "James_183", "Pythagenport", "Pythagenpat", "Palmer_RPW", "Tango_RPW", "Tango_RPW_RD"],
    "Winning Rate": [
        Cook(runs, runs_allowed),
        Soolman(runs_average, runs_allowed_average),
        James_2(runs, runs_allowed),
        James_183(runs, runs_allowed),
        Pythagenport(runs, runs_allowed, runs_per_game),
        Pythagenpat(runs, runs_allowed, runs_per_game),
        Palmer_RPW(average_runs_per_inning, average_runs_allowed_per_inning),
        Tango_RPW(runs_per_game),
        Tango_RPW_RD(runs_per_game, runs_difference)
    ]
}

# 結果をデータフレームに変換
df: pd.DataFrame = pd.DataFrame(results)

# テーブルとして表示
st.table(df)