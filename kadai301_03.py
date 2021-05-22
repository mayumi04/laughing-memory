class Mise:
    zaiko = 10
    print(f'在庫{zaiko}')

    def sale(self):
        Mise.zaiko = Mise.zaiko -1
        if Mise.zaiko > 0:
            print(f'在庫{Mise.zaiko}')
        else:
            print('在庫切れ　閉店です。')


osaka = Mise()
nagoya = Mise()
hokkaido = Mise()

while Mise.zaiko:
    print('A: 大阪店 B: 名古屋店 C: 北海道店')
    x = input('支店コードを入力してください　→　')
    
    if x == 'A':
        osaka.sale()
    elif x =='B':
        nagoya.sale()
    elif x =='C':
        hokkaido.sale()
    else:
        print('その支店はありません。')

