def msg(n, p, m, c):

    def level(p, m, c):
        return ((p * 1.5) + (m * 1.7) )* (c / 10)

    x = level(p, m, c)
    print(n + "：" + str(x))
    
    
#キャラの強さ (名前、ちから、まりょく、みりょく)
yoshihiko = msg("ヨシヒコ", 70, 30, 50)
dannjyo = msg("ダンジョ", 90, 0, 45)
murasaki = msg("ムラサキ", 10, 80, 90)
merebu = msg("メレブ", 20, 50, 5)