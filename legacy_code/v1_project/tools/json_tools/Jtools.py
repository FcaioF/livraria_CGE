from flask import jsonify

"""
biblioteca criada para desenvolver função que manipulam arquivos json

format_json(): recebe dados em formato de tupla e devolve a mesma lista em formato json

order_json_data(): recebe dados em formato json que estao desordenados e retorna a mesma lista json com ordenacao necessaria para inserir dados na tabela books
"""

#convert tuple  in json data
def format_json(raw_objects,table):
    _formated_data= list()
    for i in raw_objects:
        if (table == 'BOOK'):
            _formated_data.append(
                {
                    'ID_BOOK': str(i[0]),
                    'DT_PROCESS_DATE': i[1].strftime('%Y-%m-%d %H:%M:%S'),
                    'DS_BOOK_CATEGORY': i[2],
                    'DS_BOOK_TITLE': i[3],
                    'NR_BOOK_PRICE': i[4],
                    'DS_BOOK_DESCRIPTION': i[5],
                    'NR_UPC_NUMBER': i[6],
                    'TP_PRODUCT_TYPE': i[7],
                    'NR_NO_TAX_PRICE': float(i[8]),
                    'NR_W_TAX_PRICE': float(i[9]),
                    'NR_TOTAL_AVAILABLE': i[10],
                    'DS_BOOK_STAR': i[11],
                }
            )
        elif (table == 'CLIENTS'):
            _formated_data.append(
                {
                    'ID_CLIENT': str(i[0]),
                    'DATE_REGISTER': i[1].strftime('%Y-%m-%d %H:%M:%S'),
                    'NAME': i[2],
                    'EMAIL': i[3],
                    'DDD': i[4],
                    'CELL': i[5],
                    'CPF': i[6],
                    'COMPLEMENT':i[7],
                    'STREETS':i[8],
                    'CITY':i[9],
                    'UF': i[10],
                    'CEP': i[11]
                }
            )


    return jsonify(_formated_data)

#function used to order json data to fit in books table
def order_json_data(raw_list,table):
    _formated_json = []

    for json in raw_list:
        if (table == 'BOOK'):
            _formated_json.append(
                {
                    "DT_PROCESS_DATE": json['DT_PROCESS_DATE'],
                    "DS_BOOK_CATEGORY": json['DS_BOOK_CATEGORY'],
                    "DS_BOOK_TITLE": json['DS_BOOK_TITLE'],
                    "NR_BOOK_PRICE": json['NR_BOOK_PRICE'],
                    "DS_BOOK_DESCRIPTION": json['DS_BOOK_DESCRIPTION'],
                    "NR_UPC_NUMBER": json['NR_UPC_NUMBER'],
                    "TP_PRODUCT_TYPE": json['TP_PRODUCT_TYPE'],
                    "NR_NO_TAX_PRICE": json['NR_NO_TAX_PRICE'],
                    "NR_W_TAX_PRICE": json['NR_W_TAX_PRICE'],
                    "NR_TOTAL_AVAILABLE": json['NR_TOTAL_AVAILABLE'],
                    "DS_BOOK_STAR": json['DS_BOOK_STAR']

                }
            )
        elif(table == 'CLIENTS'):
            _formated_json.append(
                {
                    "DATE_REGISTER": json['DATE_REGISTER'],
                    "NAME": json['NAME'],
                    "EMAIL": json['EMAIL'],
                    "DDD": json['DDD'],
                    "CELL": json['CELL'],
                    "CPF": json['CPF'],
                    "COMPLEMENT": json['COMPLEMENT'],
                    "STREETS": json['STREETS'],
                    "CITY": json['CITY'],
                    "UF": json['UF'],
                    "CEP": json['CEP']

                }
            )

    return _formated_json