import pandas as pd
df = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght100lb':[138,275,413,550],
}

df100 = pd.DataFrame(df)


x1 = df100[['steps']]

y1 = df100['Burned_calories_by_wieght100lb']



#200lb 6 h 

df2 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght200lb':[273,545 ,818 ,1090]
}

df200 = pd.DataFrame(df2)


x2 = df200[['steps']]

y2 = df200['Burned_calories_by_wieght200lb']


# 300lb 6 h 

df300 = {
    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght300lb':[410 , 820 ,1230 ,1640]
}

df300 = pd.DataFrame(df300)


x3 = df300[['steps']]

y3 = df300['Burned_calories_by_wieght300lb']



# 100lb 5.6 h - 5.11 h 

dfh5_6 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght100lb':[125,250,375,500]
}

df100_h5 = pd.DataFrame(dfh5_6)


x1_1 = df100_h5[['steps']]

y1_1 = df100_h5['Burned_calories_by_wieght100lb']


# 200lb 5.6 h - 5.11 h 

dfh5_6200 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght200lb':[248,495,743,991]
}

df200_h5 = pd.DataFrame(dfh5_6200)

x1_2 = df200_h5[['steps']]

y1_2  = df200_h5['Burned_calories_by_wieght200lb']





# 300lb 5.6h - 5.11 h 

dfh5_6300 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght300lb':[373,745,1118,1491]
}

df300_h5 = pd.DataFrame(dfh5_6300)

x1_3 = df300_h5[['steps']]

y1_3 = df300_h5['Burned_calories_by_wieght300lb']




# 100lb 5.5 or less 

dfh5_5 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght100lb':[115,229,344,458]
}

df100_h5_5 = pd.DataFrame(dfh5_5)

x2_1 = df100_h5_5[['steps']]

y2_1 = df100_h5_5['Burned_calories_by_wieght100lb']



# 200lb 5.5 or less 

dfh5_5200 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght200lb':[227,454,681,908]
}

df200_h5_5 = pd.DataFrame(dfh5_5200)



x2_2 = df200_h5_5[['steps']]

y2_2 = df200_h5_5['Burned_calories_by_wieght200lb']


# 300lb 5.5 or less 

dfh5_5300 = {


    'steps':[5000,10000,15000,20000],

    'Burned_calories_by_wieght300lb':[342,683,1025,1367]
}

df300_h5_5 = pd.DataFrame(dfh5_5300)



x2_3 = df300_h5_5[['steps']]

y2_3 = df300_h5_5['Burned_calories_by_wieght300lb']
