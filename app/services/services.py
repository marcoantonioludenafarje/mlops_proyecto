#-------------------------------------------#
# Usando Peewee como ORM para las consultas
#-------------------------------------------#
# Importacion de las librerías/módulos
import pandas as pd
import numpy as np


def analize_sql(resultSQL):
    df = pd.DataFrame(resultSQL)
    # objetoResultActor = {}
    # df[ df["cast"] == "nan"].cast= "cositasLocas"
    print("Contando nan")
    # print(    df[ df["cast"] == "nan"].count())

    # df.loc[  df["cast"] == "nan" , "cast"] = ""
    
    df.cast=df.cast.str.split(',')
    print( df.info())
    print( df[["id", "cast"]].head(5))
    print("Another data")
    
    New_df=pd.DataFrame({
        'cast':np.concatenate(df.cast.values),
        'id':df.id.repeat(df.cast.apply(len))
        # 'score':df.score.repeat(df.topics.apply(len)) 
    })
    print("Aca tamoz todos1234567")
    print(New_df.head(5))
    print("Hello world NewPdf 123")
    print(New_df.iloc[0]["cast"])
    print(New_df.iloc[0]["id"])

    new_pd = New_df.groupby('cast').cast.agg(['count'])
    print(new_pd)
    sorted_df=new_pd
    # sorted_df = new_pd.sort_values(by=['count'], ascending=False)
    # sorted_df_new = sorted_df[sorted_df["cast"] != ""]

    print("Hello new world")
    countries_to_keep = ["nan"]
    print("sorted_df 123")
    print(new_pd.info())
    
    # another_df = sorted_df[~sorted_df.cast.isin(countries_to_keep)]

    
    # another_df= sorted_df[ sorted_df["cast"] != "nan" ]
    print("Hello my friend")
    print(sorted_df.info())
    print("Hello keys")
    # print(sorted_df.loc[0])


    result_df=pd.DataFrame(columns=['cast','count'])
    print("Cantidad de Newdf123")
    print(New_df.info())
    print(New_df.head(7))
    
    another_group = New_df.groupby('cast')
    print("Hola mundo 123")
    print("Cantidad de Newdf")
    # print(another_group)
    print(another_group.head(5))
    print("Lo nuevo amigito")
    print(new_pd.head(6))

    counts_df = pd.DataFrame(New_df.groupby('cast').size().reset_index(name='counts'))
    sorted_df = counts_df.sort_values(by=['counts'], ascending=False)
    print("Hacer un sorted_df df")
    print(sorted_df.head(5))
    print("Una muestra")
    print(sorted_df.head(5))
    df_clean =sorted_df[sorted_df["cast"] != "nan"]
    df_max_value = df_clean["counts"].max()
    df_movies_with_same_counts = df_clean[ df_clean["counts"] == df_max_value ]
    print("the max value df_movies_with_same_counts")
    print(df_movies_with_same_counts)
    
    return df_movies_with_same_counts.to_json()


    # for group_name, df_group in another_group:
    #     print('\nCREATE TABLE {}('.format(group_name))
        # for row_index, row in df_group.iterrows():
        #     col = row['column']
        #     column_type = row['column_type']
        #     is_null = 'NOT NULL' if row['is_null'] == 'No' else ''
        #     print('\t{} {} {},'.format(col, column_type, is_null))

    # for key, value in enumerate(sorted_df):
    #     print("El key")
    #     print(key)
    #     print("El value")
    #     print(value)
    #     # index=sorted_df.index[key]
    #     # result_df=result_df.append({'cast':index,'count':value},ignore_index=True)
    # print("El nuevo result 123")
    # print(result_df)

    # print(sorted_df.keys())
    
    # print(sorted_df.iloc[0].cast)
    # print(sorted_df.head(5))
    
    # New_df.groupby('cast').cast.agg(['count'])