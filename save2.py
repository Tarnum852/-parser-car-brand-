import pandas as pd

def save(name,brand_tipe,tag,):
    df_marks = pd.DataFrame(
        {'название бренда': name, 'тип бренда': brand_tipe, 'теги': tag })
    df_marks.to_excel('1test.xlsx')


if __name__=='__main__':
    a=[[1],[2,2]]
    b = [2,2]
    c = [3,1]
    save(a,b,c)