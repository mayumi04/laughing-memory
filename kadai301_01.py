class total:
    count = 0

    @classmethod
    def goukei(cls): 
        x = input()
        while x.isdigit():
            x = int(x)
            cls.count = cls.count + x
            print(f'合計：{cls.count}')
            x = input()
        else:
            print('終わります。')

total.goukei()