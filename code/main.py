import multiprocessing as mp
import time
import pandas as pd

from func import new_model


def func(n):
    new_model.predict(n)
    return None


if __name__ == '__main__':
    
    df = pd.read_csv('/Users/varun/Documents/data.csv')

    
    genre_features = ['num_pages', 'book_rating', 'book_price', 'text_lang']
    genre_target = 'book_genre'

    for j in [1000,10000,40000,100000]:
        
        x = df[genre_features][:j] # Chnge this to list

        s1 = time.time()
        for i in range(1,x.shape[0]):
            func(x.iloc[i-1:i].values)
        e1 = time.time()


        s2 = time.time()
        p = mp.Pool()

        result = p.map(func,[[x.iloc[k].values] for k in range(x.shape[0])])

        p.close()
        e2 = time.time()
        
        SpeedUp = (e1-s1) / (e2-s2)
        
        Efficiency = (SpeedUp / 8) *100

        print('Time taken for Serial is {a} \nTime for Parallel is {b} \nData size taken {c} \nSpeedUp is {d} \nEfficiency is {e}\n' 
              .format( a = e1-s1, b = e2-s2, c = j , d = SpeedUp, e = Efficiency))
