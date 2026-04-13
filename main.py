#毎回やっておく
#git add .
#git commit -m "更新"
#git push origin main

import time
import os
import random
#道路の長さ
ROAD_LENGTH = 90
#信号の位置
SIGNAL_POSITIONS = [20, 40, 60]  # 3箇所に設置
signal_states = ["RED", "RED", "RED"] # 初期の状態
signal_timers = [0, 1, 2]           # それぞれのタイマー

def run_simulation():
    road = [0] * ROAD_LENGTH
    step = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # ランダム車両生成
        if road[0] == 0 and random.random() < 0.3:
            road[0] = 2 if random.random() < 0.1 else 1

        # 各信号機の状態更新
        for i in range(len(SIGNAL_POSITIONS)):
            signal_timers[i] += 1
            if signal_timers[i] >= 15:
                signal_states[i] = "GREEN" if signal_states[i] == "RED" else "RED"
                signal_timers[i] = 0

        #移動
        new_road = [0] * ROAD_LENGTH
        for i in range(ROAD_LENGTH - 1, -1, -1):
            if road[i] > 0:
                next_pos = i + 1
                
                # 道路の終端
                if next_pos >= ROAD_LENGTH:
                    continue
                
                # 信号判定
                stop_at_signal = False
                for j, pos in enumerate(SIGNAL_POSITIONS):
                    if i == pos - 1 and signal_states[j] == "RED":
                        stop_at_signal = True

                    
                
                #new_road[next_pos] を見て既に移動した前の車がそこにいるかどうかを確認する
                car_ahead = (new_road[next_pos] > 0)
                
                if stop_at_signal or car_ahead:
                    new_road[i] = road[i]
                else:
                    new_road[next_pos] = road[i]
        
        road = new_road

#表示
        upper_line = list(" " * ROAD_LENGTH) # 信号表示用の上の行
        road_line = list("□" * ROAD_LENGTH)  # 実際の道路

        #信号機の表示
        for j, pos in enumerate(SIGNAL_POSITIONS):
            upper_line[pos] = "🔴" if signal_states[j] == "RED" else "🟢"
            # 道路側目印
            road_line[pos] = "｜" if road[pos] == 0 else road_line[pos]

        #車の表示
        for i in range(ROAD_LENGTH):
            if road[i] == 1: 
                road_line[i] = "■"
            elif road[i] == 2: 
                road_line[i] = "△"

        print(f"Step: {step}")
        print("".join(upper_line)) # 上の行を表示
        print("".join(road_line))  # 下の行を表示
        
        step += 1
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()


    