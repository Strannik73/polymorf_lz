import pandas as pd


class sumop:

    def __init__(self):
        self.df = pd.read_csv('var3.csv')

    def __neg__(self):
        return self.df.drop_duplicates()
    print('количество удаленных дубликатов:  ' ,  ,)

    def dann(self):
        df = -self.df
        
    def delen(self):
        df1 = self.df[self.df['Сумма cash-back'] <= 1000.00]    # строки, удовлетворяющие условию
        df2 = self.df[self.df['Сумма cash-back'] > 1000.00]  

