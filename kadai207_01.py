def standup():
    print("【玄関に向かう】\n立ち上がる\n廊下を歩く\n扉を開ける\n")

def go_walk():
    print("【買いに行く】\n道を歩く\nお金を入れる\n飲み物を選択する\n")

def go_bicycle():
    print("【買いに行く】\
        \n自転車に乗る\nコンビニに向く\n自転車を走らせる\
        \nコンビニに入る\n飲み物を選択する\nレジに向かう\nお金を払う\n")

def back_walk():
    print("【戻る】\n道を歩く\n扉を開ける\n廊下を歩く\n")

def back_bicycle():
    print("【戻る】\
        \n自転車に乗る\n自宅に向く\n自転車を走らせる\n扉を開ける\n廊下を歩く\n")

def drink():
    print("【飲む】\n栓を開ける\n飲む")


x = input("なにを飲みますか？1:　コーラ　2:　ポーション")
standup()
if x == "1":
    go_walk()
    back_walk()
elif x == "2":
    go_bicycle()
    back_bicycle()
drink()