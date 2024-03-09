#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from premailer import transform
import json
from utils.clean import Clean
from utils.paint import Paint
from utils.send import Send


def main():

    try:

        clean = Clean()
        paint = Paint()
        send = Send()

        def background_index1(col):
            styles = []
            for col_name in col:
                if col_name in ['restaurant_id', 'restaurant_name']:
                    styles.append('background-color: #DCDCDC')
                elif col_name in ['country', 'city', 'cuisines']:
                    styles.append('background-color: #F0E68C')   
                elif col_name in ['aggregate_rating', 'votes']:
                    styles.append('background-color: #B0C4DE')  
                elif col_name in ['average_cost_for_two', 'custo']:
                    styles.append('background-color: #8FBC8F')          
                else:
                    styles.append('')
            return styles

        #Extract
        with open('caminho-para-o-json-com-a-senha') as f:
            user = json.load(f)
        df = pd.read_csv('./data/zomato.csv')

        #Transform
        df = clean.rename_columns(df)
        df['country'] = df['country_code'].apply(clean.country_name)
        dados = df.loc[:,['restaurant_id','restaurant_name','country_code','country' ,'city','cuisines','average_cost_for_two', 'aggregate_rating','votes']]\
                        .sort_values('aggregate_rating',ascending=False)

        relatorio = dados.head(10)
        relatorio['custo'] = '$'
        relatorio = relatorio[['restaurant_id',
                        'restaurant_name',
                        'country', 
                        'city', 
                        'cuisines',
                        'aggregate_rating', 
                        'votes',
                        'average_cost_for_two', 
                        'custo']]
        
        styled_df = relatorio.style \
                            .apply(paint.background_color1, subset=pd.IndexSlice[:, ['restaurant_id', 'restaurant_name']]) \
                            .apply(paint.background_color2, subset=pd.IndexSlice[:, ['country', 'city', 'cuisines']]) \
                            .apply(paint.background_color3, subset=pd.IndexSlice[:, ['aggregate_rating', 'votes']]) \
                            .apply(paint.background_color4, subset=pd.IndexSlice[:, ['average_cost_for_two', 'custo']]) \
                            .apply(lambda col: col.apply(lambda x: paint.style_by_cost(x, col['average_cost_for_two'])), subset=['custo', 'average_cost_for_two'], axis=1) \
                            .apply(paint.text_color, subset=pd.IndexSlice[:, ['restaurant_id', 'restaurant_name', 'country', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']]) \
                            .apply_index(background_index1, axis='columns')\
                            .apply_index(paint.text_color, axis='columns')\
                            .hide_index()
        
        html_table = styled_df.render()
        html_with_css = transform(html_table)

        #Send
        subjetct = 'Relatorio de Restaurantes'
        corpo_email = f"""
                        <title> Relatorio de Restaurantes </title>

                        <h1> Melhores Restaurantes </h1>
                        {html_with_css}
                        """

        send.send_mail(corpo_email, 'destinatario', user['email'], user['senha'],subjetct)



    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()