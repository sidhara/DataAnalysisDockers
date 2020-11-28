import dash
import dash_core_components as dcc
import dash_html_components as html
import mysql.connector
#import seaborn as sns
#import matplotlib.pyplot as plt

connection=mysql.connector.connect(host='sql',user='sloth',passwd='sloth')
cursor=connection.cursor()
cursor.execute("select MES, CHOQUE_CON_LESIONADO from database.cali")
mes1=cursor.fetchone()#usar format
mes2=cursor.fetchone()
mes3=cursor.fetchone()
mes4=cursor.fetchone()
mes5=cursor.fetchone()
mes6=cursor.fetchone()
mes7=cursor.fetchone()
mes8=cursor.fetchone()
mes9=cursor.fetchone()
mes10=cursor.fetchone()
mes11=cursor.fetchone()
mes12=cursor.fetchone()

cursor.execute("select MES, FALSA_ALARMA from database.cali")
mes1b=cursor.fetchone()#usar format
mes2b=cursor.fetchone()
mes3b=cursor.fetchone()
mes4b=cursor.fetchone()
mes5b=cursor.fetchone()
mes6b=cursor.fetchone()
mes7b=cursor.fetchone()
mes8b=cursor.fetchone()
mes9b=cursor.fetchone()
mes10b=cursor.fetchone()
mes11b=cursor.fetchone()
mes12b=cursor.fetchone()

cursor.execute("select MES, SOLO_DANOS from database.cali")
mes1c=cursor.fetchone()#usar format
mes2c=cursor.fetchone()
mes3c=cursor.fetchone()
mes4c=cursor.fetchone()
mes5c=cursor.fetchone()
mes6c=cursor.fetchone()
mes7c=cursor.fetchone()
mes8c=cursor.fetchone()
mes9c=cursor.fetchone()
mes10c=cursor.fetchone()
mes11c=cursor.fetchone()
mes12c=cursor.fetchone()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

name = 'main'

app = dash.Dash(name, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  html.H1(children='Estadisticas de Accidentalidad en Cali 2019'),

  html.Div(children='''
    Estructura del computador 2:	
    Sidhar Araujo 200106255,	
    Jorge Riaño 200106765,
    Carlos Menassa 200109166,
    Daniel Martinez 200107915	
  '''),

  dcc.Graph(
    id='lesiones',
    figure={
      'data': [
        {'x': [format(mes1[0]), format(mes2[0]), format(mes3[0]), format(mes4[0]), format(mes5[0]), format(mes6[0]), format(mes7[0]), format(mes8[0]), format(mes9[0]), format(mes10[0]), format(mes11[0]), format(mes12[0])], 'y': [format(mes1[1]), format(mes2[1]), format(mes3[1]), format(mes4[1]), format(mes5[1]), format(mes6[1]), format(mes7[1]), format(mes8[1]), format(mes9[1]), format(mes10[1]), format(mes11[1]), format(mes12[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Accidentes con lesiones'
      }
    }
  ),
  dcc.Graph(
    id='falsa-alarma',
    figure={
      'data': [
        {'x': [format(mes1b[0]), format(mes2b[0]), format(mes3b[0]), format(mes4b[0]), format(mes5b[0]), format(mes6b[0]), format(mes7b[0]), format(mes8b[0]), format(mes9b[0]), format(mes10b[0]), format(mes11b[0]), format(mes12b[0])], 'y': [format(mes1b[1]), format(mes2b[1]), format(mes3b[1]), format(mes4b[1]), format(mes5b[1]), format(mes6b[1]), format(mes7b[1]), format(mes8b[1]), format(mes9b[1]), format(mes10b[1]), format(mes11b[1]), format(mes12b[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Falsa Alarma'
      }
    }
  ),
  dcc.Graph(
    id='daños',
    figure={
      'data': [
        {'x': [format(mes1c[0]), format(mes2c[0]), format(mes3c[0]), format(mes4c[0]), format(mes5c[0]), format(mes6c[0]), format(mes7c[0]), format(mes8c[0]), format(mes9c[0]), format(mes10c[0]), format(mes11c[0]), format(mes12c[0])], 'y': [format(mes1c[1]), format(mes2c[1]), format(mes3c[1]), format(mes4c[1]), format(mes5c[1]), format(mes6c[1]), format(mes7c[1]), format(mes8c[1]), format(mes9c[1]), format(mes10c[1]), format(mes11c[1]), format(mes12c[1])], 'type': 'bar', 'name': 'SF'},
      ],
      'layout': {
        'title': 'Solo Daños'
      }
    }
  )
])

if name == 'main':
  app.run_server(host='0.0.0.0', port=8080, debug=True)