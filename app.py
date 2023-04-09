
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
import xlrd
import numpy as np

#pd.set_option('display.float_format', lambda x: '%.6f' % x)



# https://htmlcheatsheet.com/css/

##### LOADING THE DATA #######################################################################################
path = 'https://raw.githubusercontent.com/Denzelbasso/Data-Visualisation/main/dataset/'
#Dataframes of specific quantities imported by nation
pt_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 por Portugal, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
es_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 por Espanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
fr_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 pela Franca, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
de_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 pela Alemanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
it_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 pela Italia, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of overall quantities imported by nation
w_qimp = pd.read_excel((path + 'ITC - Lista da quantidade importada do produto 2204 por Paises, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")

#Dataframes of specific value imported by nation
pt_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 por Portugal, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
es_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 por Espanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
fr_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 pela Franca, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
de_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 pela Alemanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
it_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 pela Italia, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of overall value imported by nation
w_vimp = pd.read_excel((path + 'ITC - Lista do valor importado do produto 2204 por Paises, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of specific quantities exported by nation
pt_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 por Portugal, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
es_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 por Espanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
fr_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 pela Franca, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
de_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 pela Alemanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
it_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 pela Italia, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of overall quantities exported by nation
w_qexp = pd.read_excel((path + 'ITC - Lista da quantidade exportada do produto 2204 por Paises, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of specific value exported by nation
pt_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 por Portugal, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
es_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 por Espanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
fr_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 pela Franca, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
de_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 pela Alemanha, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
it_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 pela Italia, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Dataframes of overall quantities exported by nation
w_vexp = pd.read_excel((path + 'ITC - Lista do valor exportado do produto 2204 por Paises, entre 2003-2022.xlsx').replace(" ", "%20"), sheet_name = "Folha1")
#Function to remove empty lines
def df_fixer_qimp(df, n, exi):
    index_list = range(n)
    df.drop(df.index[index_list], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df = df.replace("No Quantity", np.nan)
    df = df.replace(0, np.nan)
    df = df.astype(str)
    df = df.set_index(exi)
    df = df.drop(exi)
    df = df.iloc[1:]
    df = df.astype(float)
    return df

def df_fixer_wqimp(df, n, exi):
    index_list = range(n)
    df.drop(df.index[index_list], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df = df.replace("No Quantity", np.nan)
    df = df.replace(0, np.nan)
    df = df.astype(str)
    df = df.set_index(exi)
    df = df.drop(exi)
    df = df.iloc[1:]
    df = df.iloc[:, np.arange(len(df.columns)) % 2 == 0]
    df = df.astype(float)
    return df

def df_fixer_wqimp2(df, n, exi):
    index_list = range(n)
    df.drop(df.index[index_list], inplace=True)
    df = df.rename(columns=df.iloc[0])
    df = df.replace("No Quantity", np.nan)
    df = df.replace(0, np.nan)
    df = df.astype(str)
    df = df.set_index(exi)
    df = df.drop(exi)
    df = df.iloc[1:]
    df = df.astype(float)
    return df

def df_fixer_vimp(df, n, exi, column_retriever):
    index_list = range(n)
    df.drop(df.index[index_list], inplace=True)
    df.columns=df.iloc[0]
    df.columns = df.columns.str.replace(column_retriever, '')
    df = df.set_index(exi)
    df = df.iloc[1:]
    df = df.astype(float)
    return df
##### NEW DFS ################################################################################################
#######Value imported
#By country
pt_vimp = df_fixer_vimp(pt_vimp ,14, "Exporters", 'Imported value in ')
fr_vimp = df_fixer_vimp(fr_vimp ,13, "Exporters", 'Imported value in ')
es_vimp = df_fixer_vimp(es_vimp ,14, "Exporters", 'Imported value in ')
de_vimp = df_fixer_vimp(de_vimp ,13, "Exporters", 'Imported value in ')
it_vimp = df_fixer_vimp(it_vimp ,13, "Exporters", 'Imported value in ')
#World
w_vimp = df_fixer_wqimp2(w_vimp ,12, "Importers")
w_vimp.columns = w_vimp.columns.str.replace('Imported value in ', '')
#######Value exported
#By country
pt_vexp = df_fixer_vimp(pt_vexp ,14, "Importers", 'Exported value in ')
fr_vexp = df_fixer_vimp(fr_vexp ,13, "Importers", 'Exported value in ')
es_vexp = df_fixer_vimp(es_vexp ,14, "Importers", 'Exported value in ')
de_vexp = df_fixer_vimp(de_vexp ,13, "Importers", 'Exported value in ')
it_vexp = df_fixer_vimp(it_vexp ,13, "Importers", 'Exported value in ')
#World
w_vexp = df_fixer_wqimp2(w_vexp ,12, "Exporters")
w_vexp.columns = w_vexp.columns.str.replace('Exported value in ', '')
#########Quantity imported
#By country
pt_qimp = df_fixer_qimp(pt_qimp, 13, "Exporters")
es_qimp = df_fixer_qimp(es_qimp, 13, "Exporters")
fr_qimp = df_fixer_qimp(fr_qimp, 12, "Exporters")
de_qimp = df_fixer_qimp(de_qimp, 12, "Exporters")
it_qimp = df_fixer_qimp(it_qimp, 12, "Exporters")
#World
w_qimp = df_fixer_wqimp(w_qimp, 12, "Importers")
w_qimp = w_qimp.iloc[1:]
##########Quantity exported
#By country
pt_qexp = df_fixer_qimp(pt_qexp, 14, "Importers")
es_qexp = df_fixer_qimp(es_qexp, 14, "Importers")
fr_qexp = df_fixer_qimp(fr_qexp, 13, "Importers")
de_qexp = df_fixer_qimp(de_qexp, 13, "Importers")
it_qexp = df_fixer_qimp(it_qexp, 13, "Importers")
#World
w_qexp = df_fixer_wqimp(w_qexp, 12, "Exporters")
w_qexp = w_qexp.iloc[1:]
#Creating the unique df
def create_dataframe(country):
    c = w_vexp.T
    d = w_qexp.T
    d = d.reset_index()

    e = w_vimp.T
    e = e.reset_index()

    f = w_qimp.T
    f = f.reset_index()

    c_country = c[country]

    df = pd.DataFrame({'Country': np.repeat(country, len(c_country)), c_country.index.name: c_country.index.values, c_country.name: c_country.values})

    df = df.rename(columns={0: 'Country', 'Year': 'Year', 1: 'Export value'})
    df.columns = ['Country', 'Year', 'Export value']

    df['Export quantity'] = d[country]
    df['Import value'] = e[country]
    df['Import quantity'] = f[country]

    return df
countries = ["Portugal", "Spain", "France", "Germany", "Italy"]

dfs = []

for country in countries:
    df = create_dataframe(country)
    dfs.append(df)

df = pd.concat(dfs)

df['Year'] = df['Year'].astype(int)

# create the list of possible countries
country_options = ['Portugal', 'Spain', 'Italy', 'Germany', 'France']
# create the list of possible types of transactions
multiple_country_options = ['Portugal', 'Spain', 'Italy', 'Germany', 'France']

#Second df for export by top country
def graph2(country, df):
    df2best = pd.DataFrame()
    df = df.T
    for i in range(1, 20):
        df2 = pd.DataFrame(
            {'Countries': country, "Export": df.columns[i], "Year": df.index, 'Export Value': df.iloc[:, i]})
        new_series = df2['Export Value']
        df2.reset_index()
        df2best = df2best.append(df2, ignore_index=True)

    return df2best
es_df2 = graph2("Spain", es_vexp)
pt_df2 = graph2("Portugal", pt_vexp)
fr_df2 = graph2("France", fr_vexp)
de_df2 = graph2("Germany", de_vexp)
it_df2 = graph2("Italy", it_vexp)

df2 = pd.concat([es_df2, pt_df2, fr_df2, de_df2, it_df2], ignore_index=True)
df2['Year'] = df2['Year'].astype(int)


##### APP #####################################################################################################
# Data Preprocessing


# List of fixed Plots - no filter applied
# token to use a free type of map from mapbox - style: light
mapbox_token = 'pk.eyJ1IjoiYW5hYmVhdHJpemZpZyIsImEiOiJjbDF0NXZ4dW4yNjFrM2pxcnp1ZzQ1cGl1In0.vpjAAtkv4flG_jtgOHcDQw'

# 1-MAP
def map():
    fig = go.Figure(data=go.Choropleth(
        locations=w_vexp.index,
        locationmode='country names',
        z=np.log(w_vexp.iloc[:, -2]),  # Use iloc to select the last column as an array
        text=w_vexp.index,
        colorscale=[[0, '#F4C2C2'], [1, '#9B1B30']]
    ),
        layout=dict(geo=dict(scope='world',
                             showland=True,
                             landcolor='#D3D3D3',
                             lakecolor='white',
                             showocean=True,
                             oceancolor='azure'
                            )
        )
    )

    fig.update_layout(
        plot_bgcolor='#F4D3CA', paper_bgcolor='#F4D3CA',
        title_font=dict(size=20, color='white', family="Times New Roman"),
        font=dict(color='black', family="Times New Roman"),
        sliders=[dict(
            currentvalue=dict(prefix='Year: ', font=dict(size=14, family='Times New Roman', color="black")),
            active=len(w_vexp.columns) - 2,
            pad=dict(t=10),
            steps=[dict(
                label=str(year),
                method='update',
                args=[{'z': [np.log(w_vexp.iloc[:, year - 2003])]}],
            )
                for year in range(2003, 2023)],
        )],
    )

    return fig


################################ Construction of the App
app = dash.Dash(__name__)

server = app.server

# Layout and styles using css file
app.layout = html.Div([
    html.Div([
        html.H1('Wine exportation – Top 5 European exporters',
                style={'font-family': 'New Times Roman', 'color': 'Black', 'margin-bottom': '60px'}),

        html.Div([
            html.P('The goal of this dashboard is to develop an interactive visualisation of data about the exportation of wine by value. The dashboard will enable the user to analyse the top 5 European exporters by value in depth. It’s divided into 2 parts:',
                   style={'color': 'Black', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
            html.P('-1st: an individual view of each country’s export value with graph 1 and 2.',
                   style={'color': 'Black', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
            html.P('-2nd: a comparative analysis between the countries’ export value with graph 3 and image 1.',
                   style={'color': 'Black', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
            html.P('First, the user is provided with the option to select a range of years to analyze, starting from 2003 up to 2022, and also choose a country of interest. Graph 1 exhibits the trend of wine export and import value over the years, indicating their respective growth and comparison. In addition, Graph 2 displays the top 6 countries that the selected country exports the highest value in the year chosen from the slider.',
                   style={'color': 'Black', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
        ], className='column_two_filter'),


    ], style={'margin-top': '0'})  # Add style attribute to set margin-top to 0

    ,
    html.Div([
        html.Div([
            html.Div([html.Label('Year:', style={'font-family': 'Times New Roman'}),
                      dcc.Slider(
                          id='year_slider',
                          min=df['Year'].min(),
                          max=df['Year'].max(),
                          marks={str(i): '{}'.format(str(i)) for i in
                                 [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,2022]},
                          value=2022,
                          step=1,
                          className='slider')],
                     className='column_two_filter'
                     ),
            html.Div([html.Label('Country:', style={'font-family': 'Times New Roman'}),
                      dcc.Dropdown(
                          id='country_drop',
                          options=country_options,
                          value='Portugal',
                          multi=False
                      )],
                     className='column_two_filter'
                     )],
            className='row')
    ], className='filter'),
    html.Div([
        html.Div([
            html.H2(children='Graph 1. - Evolution of the value of export and import of wine of the selected country, in thousands of euros', style={'font-family': 'Times New Roman'}),
            dcc.Graph(id='fig_line_up'),
            html.H3(children='Source: International Trade Center 2023', style={'font-family': 'Times New Roman'})
        ], className='column_two'),
        html.Div([
            html.H2(
            children='Graph 2. - Top 6 countries that the selected country exports the most wine to by value, in thousands of euros',
            style={'font-family': 'Times New Roman'}),
            dcc.Graph(id='bar_chart_plot'),
            html.H3(children='Source: International Trade Center 2023', style={'font-family': 'Times New Roman'})
        ],
            className='column1'
        )
    ],

        className='row'),
    html.Div([
        html.Div([
            html.P('The goal of this dashboard is',
                   style={'color': '#F4D3CA', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
            html.P('Second, the user has the option to compare the value of wine exportation between a selection of the 5 countries, shown in graph 3, within the time frame of 2003 to 2022. ',
                   style={'color': 'black', 'line-height': '2', 'font-family': 'New Times Roman',
                          'text-align': 'justify'},
                   className='paragraph'),
            html.P(
                'Moreover, the user can view the global export value of wine of any specific country in the year selected on the slider of image 1. This map highlights how the 5 countries compare with the rest of the world.',
                style={'color': 'black', 'line-height': '2', 'font-family': 'New Times Roman',
                       'text-align': 'justify'},
                className='paragraph'),


        ], className='paragraph')
    ], style={'margin-top': '0'})  # Add style attribute to set margin-top to 0
,
    html.Div([
        html.Div([
            html.Div([
                html.Label('Countries confrontation:'),
                dcc.Dropdown(
                    id='type_country',
                    options=multiple_country_options,
                    value=multiple_country_options,
                    multi=True
                )
            ])
        ], className='column_two_filter'),
        html.Div([
            # This div is left empty
        ], className='column_two_filter')
    ], className='row'),
    html.Div([
        html.Div([
            html.H2(children='Graph 3. - Evolution of the value of export of wine of the selected countries between 2003 to 2022, in thousands of euros', style={'font-family': 'Times New Roman'}),
            dcc.Graph(id='fig_line_down'),
            html.H3(children='Source: International Trade Center 2023', style={'font-family': 'Times New Roman'})
        ], className='column_two'),
        html.Div([
            html.H2(children='Image 1. - World map of value exported of wine by country, in thousands of euros',
                    style={'font-family': 'Times New Roman'}),
            dcc.Graph(id='map',
                      figure=map()
                      ),
            html.H3(children='Source: International Trade Center 2023', style={'font-family': 'Times New Roman'})
        ],
            className='column1'
        ),
        html.Div([html.H4(children='')], className='row'),
    ],
        className='row'),

    html.Br(),
    html.Br(),
    html.Div([
        html.P(
            'Authors: André Dias, n.20220636; Denzel Basso n.20220671; Ricardo Coelho n.20220691',
            style={'color': 'black', 'font-family': 'Times New Roman'}),
        html.P('Dataset:', style={'color': 'black', 'font-family': 'Times New Roman'}),
        html.A('GitHub Countries Transaction Dataset',
               href='https://github.com/Denzelbasso/Data-Visualisation',
               style={'color': 'black', 'font-family': 'Times New Roman'}),
    ],
        className='paragraph')

])


# Line Plots with responsive filters
# 1-Line Plot - Renewable and No Renewable Energy Consumption
# Filters: years and country
@app.callback(
    Output('fig_line_up', 'figure'),
    Input('country_drop', 'value'),
    Input('year_slider', 'value'),
)
def plots(countries, year):
    data = df[['Country', 'Year', 'Export value', 'Import value']]
    variables = ['Export value', 'Import value']
    country = countries
    year = list(range(2003, year+1))
    data_filter = data.loc[(data['Country'] == country) & (data['Year'].isin(year))]

    data_line = []

    for i, variable in enumerate(variables):
        x_line = data_filter['Year']
        y_line = data_filter[variable]
        line_color = '#A50F15' if i == 0 else '#5AF0EA'

        data_line.append(dict(
            type='scatter',
            mode='lines',
            x=x_line,
            y=y_line,
            text=y_line.name,
            customdata=data_filter['Country'],
            name=variable,
            hovertemplate="<b>Country: </b> %{customdata} <br>" +
                          "<b>Year: </b> %{x} <br>" +
                          "<b>Value: </b> %{y} Twh<br>",
            line=dict(color=line_color)
        ))

    layout_line = dict(
        xaxis=dict(
            tickfont=dict(family='Times New Roman', color='black'),
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            zeroline=True,
            linecolor='lightgray',
            linewidth=1
        ),
        yaxis=dict(
            title='Thousands of euros',
            tickfont=dict(family='Times New Roman', color='black'),
            showgrid=True,
            gridcolor='lightgray'
        ),
        legend=dict(
            orientation="h",
            font=dict(family='Times New Roman')
        ),
        margin=dict(l=40, r=40, b=20, t=5),
        plot_bgcolor='#F9F9F9',
        paper_bgcolor='#F4D3CA'
    )

    fig_bar = go.Figure(data=data_line, layout=layout_line)
    fig_bar.update_yaxes(showgrid=False)

    return fig_bar



# 2-Line Plot - Comparison of countries export value
# Filters: country
@app.callback(
    Output('fig_line_down', 'figure'),
    Input('type_country', 'value')
)
def plots(countries):
    data = df[['Country', 'Year', 'Export value']]
    # selecting the variables of each line
    variables = countries
    # define tha max year from the filter
    year = list(range(2003, 2022))

    data_line = []
    colors = ['#A50F15', '#5AF0EA', '#00FF7F', '#A5668B', '#F9DC5C']

    data_filter = data.loc[(data['Year'].isin(year))]
    for i, variable in enumerate(variables):
        # create the filtered dataset
        data_filter = data.loc[(data['Country'] == variable)]
        x_line = data_filter['Year']
        y_line = data_filter['Export value']

        line_color = colors[i] if i < len(colors) else '#000000'  # set black color for any line beyond the length of colors

        data_line.append(dict(type='scatter',
                              mode='lines',
                              x=x_line,
                              y=y_line,
                              text=y_line.name,
                              customdata=data_filter['Country'],
                              name=variable,
                              line=dict(color=line_color),  # set the line color
                              hovertemplate="<b>Country: </b> %{customdata} <br>" +
                                            "<b>Year: </b> %{x} <br>" +
                                            "<b>Value: </b> %{y} Twh<br>")
                         )

        layout_line = dict(
            xaxis=dict(
                tickfont=dict(family='Times New Roman', color='black'),
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                zeroline=True,
                linecolor='lightgray',
                linewidth=1,
                tickvals=[2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022]
            ),
            yaxis=dict(title='Thousands of euros', titlefont=dict(family='Times New Roman', color='black')),
            legend=dict(orientation="h"),
            font=dict(family='Times New Roman', color='black'),
            margin=dict(l=40, r=40, b=20, t=5),
            plot_bgcolor='#F9F9F9',
            paper_bgcolor='#F4D3CA'
        )

    fig_bar = go.Figure(data=data_line, layout=layout_line)
    fig_bar.update_yaxes(showgrid=False)
    return fig_bar



# 3-BAR-PLOT
@app.callback(
    Output('bar_chart_plot', 'figure'),
    Input('country_drop', 'value'),
    Input('year_slider', 'value')
)
def plots(countries, year):
    data = df2
    # selecting the variables of each line
    variables = ['Export Value']
    # define the country on the filter
    country = countries
    # create the filtered dataset
    data_filter = data.loc[(data['Countries'] == country) & (data['Year'] == year)]
    data_filter = data_filter.sort_values('Export Value', ascending=False)
    data_filter = data_filter.iloc[0:6, :]
    data_bar = []
    color = '#A50F15' # set color for this bar

    data_bar.append(dict(type='bar',
                    x=data_filter['Export'],
                    y=data_filter['Export Value'],
                    name='Export Value',
                    showlegend=False,
                    marker=dict(color=color)  # set color for this bar
                    )
                )

    layout_bar = dict(

        xaxis=dict(
            tickfont=dict(family='Times New Roman', color='black'),
            showgrid=False,
            gridcolor='lightgray',
            gridwidth=1,
            zeroline=True,
            linecolor='lightgray',
            linewidth=1
        ),

        yaxis=dict(title='Thousands of euros', tickfont=dict(family='Times New Roman')),
        legend=dict(orientation="h"),
        font=dict(color='black', family='Times New Roman'),
        margin=dict(l=40, r=40, b=20, t=5),
        plot_bgcolor='#F9F9F9',
        paper_bgcolor='#F4D3CA',
    )

    #     fig = dict(data=data_bar, layout=layout_bar)

    fig_bar = go.Figure(data=data_bar, layout=layout_bar)
    fig_bar.update_yaxes(showgrid=False)
    return fig_bar

###############################################################################################################

if __name__ == '__main__':
    app.run_server(debug=True) 