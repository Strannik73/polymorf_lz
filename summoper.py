import pandas as pd
#from __ import __


class sumop:
    def __init__(self, data): 
        self.data = data
        self.df = pd.read_csv('var3.csv')
       
    def __neg__(self):
        return  self.df.drop_duplicates()  
    
    def dann(self):
        self.df = sumop('var3.csv')

        self.df = -self.df

        self.df1 = self.df[self.df['Сумма cash-back'] <= 1000.00]    
        self.df2 = self.df[self.df['Сумма cash-back'] > 1000.00]  

        print('количество удаленных строк:  ' ,100001 - (len(self.df1) + len(self.df2)),)
        self.df1.to_csv('df1.csv')
        self.df2.to_csv('df2.csv')
        
    def __del__(self):
        print('удаление')


def main():
    smop = sumop('var3.csv')
    smop.dann()

if __name__ == '__main__':
    main()