import firebase_admin
from firebase_admin import db
from firebase_admin import firestore
import pandas as pd
import json
import re
import time
import datetime
from datetime import date
import insert_data as insert
import setup_firebase as sf   

def main():
    sf.setup()

    db = firestore.client()
    sales = db.collection(u'sales')

    #Retrieve Data from firestore
    print('Para generar el reporte de ventas es necesario que ingrese un rango de fechas')   
    
    #Get the minimun and maximum date
    lowest_date = sales.order_by('InvoiceDate', direction=firestore.Query.ASCENDING).limit(1).stream()
    highest_date = sales.order_by('InvoiceDate', direction=firestore.Query.DESCENDING).limit(1).stream()

    for i in lowest_date:
        for f in highest_date:
            first_date = i.to_dict()['InvoiceDate']
            second_date = f.to_dict()['InvoiceDate']

            print(f'Rango de fechas disponibles desde \n{first_date} \nhasta \n{second_date} \n')

    while True:
        try:
            start_date_input = input('Ingresa la primera fecha del rango usando el formato YYYY-MM-DD: \n') 
            year, month, day = map(int, start_date_input.split('-'))
            start_date = datetime.datetime(year,month,day)
            
            end_date_input = input('Ingresa la segunda fecha del rango usando el formato YYYY-MM-DD: \n') 
            year, month, day = map(int, end_date_input.split('-'))
            end_date = datetime.datetime(year,month,day)

        except:
            print('Error en la fecha. \n')
            continue
        else:
            break

    #Get the data from firestore based on the date range
    dates = sales.where(u'InvoiceDate', u'>=', start_date).where('InvoiceDate', '<=', end_date).stream()
    
    #This variable will check if the stream from firestore is empty
    stream_empty = True
    data_extracted = []

    for value in dates:
        stream_empty = False
        data_extracted.append(value.to_dict())

    #Pandas Dataframe creation
    df = pd.DataFrame(data_extracted)
    df = df.sort_values(by=['InvoiceDate'])
    #Change the date type
    df['InvoiceDate'] = df['InvoiceDate'].apply(lambda a: pd.to_datetime(a).date())

    #Removing the negative values
    df = df[df['Quantity'] > 0].dropna()

    today = date.today()
    df.to_excel(f"./excel/report_{today}.xlsx", index=False ,header=True)

    if stream_empty:
        print('\nNo se encontraron datos entre ese rango de fechas.')
    else:
        print('\nExcel Generado')
    
if __name__ == "__main__":
    main()
