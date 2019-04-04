### Application Web pour la visualisation des données du Baromètre
### Utilisant Dash, Plotly 
### V.1.0.0
### Thomas Vaquero, Robin Devooght

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py 
import plotly.graph_objs as go

average_E = [31.0, 30.8, 31.1, 30.7, 30.8]
m = 0
for x in average_E:
	m = m + x
m = m / 5

average_ETP = [22.6, 22.2, 22.5, 22.4, 22.5]
n = 0
for x in average_ETP:
	n = n + x
n = n / 5



app = dash.Dash(__name__)

app.layout = html.Div([
		
	
	html.Div([
		html.Div([
			
				html.Div('Résultats du baromètre de associations et des fondations',style = {'color':'whitesmoke', 'fontSize': 30, 'textAlign':'center', 'padding':'20px'}),
				html.P('établis le 30/01/2019', style = {'textAlign':'center', 'color':'whitesmoke'}),
				html.P('Les chiffres présentés ci-dessous sont issus de la période 2013-2017, selon les sources BelFirst (Bureau Van Dijk) et ONSS',style = {'color':'snow', 'textAlign':'center', 'padding':'20px'}),

			
			html.Div([

				
				html.Div([
					html.P('Régions:', style = {'color':'goldenrod'}),
					dcc.Dropdown(
					id = 'régions',
					style = {'width':'350px', 'backgroundColor':'floralwhite'},
					options=[
						{'label': 'Flandres', 'value': 'Flandre'},
						{'label': 'Wallonie', 'value': 'Wallonie'},
						{'label': 'Bruxelles', 'value': 'Bruxelles'}
						
					],
					#value=' ',
					multi = 'True'
					)
				]),
				
				html.Div([
					html.P('Secteur:', style = {'color':'goldenrod'}),
					dcc.Dropdown(
					id = 'secteurs',
					style = {'width':'350px', 'backgroundColor':'floralwhite'},
					options=[
						{'label': 'Social', 'value': 'Social'},
						{'label': 'Santé', 'value': 'Santé'},
						{'label': 'Culture', 'value': 'Culture'},
						{'label': 'Environnement', 'value': 'Environnement'},
						{'label': 'Coopération', 'value':'Coopération'}
					],
					#value=' ',
					multi = 'True'
					)
				]),

				html.Div([

					html.P('Taille', style = {'color':'goldenrod'}),
					dcc.Dropdown(
						id = 'taille',
						style = {'width':'350px', 'backgroundColor':'floralwhite'},
						options = [
							{'label':'Petite', 'value':'Petite'},
							{'label':'Grande', 'value':'Grande'},
							{'label':'Très Grande', 'value': 'Très Grande'}
						],
						multi = 'True'
					)

				])
				

			], id = "filtres"),

		], id = "header"),


	

		html.Div('Répartition des associations et des fondations selon plusieurs critères:', style = {'color':'SteelBlue', 'fontSize':20, 'textAlign':'center', 'paddingTop': 50}),

		html.Div([

			#Graph de la répartition par taille
			dcc.Graph(
				id = 'graph_tailles',
				style = {'height': 400, 'width': 600},
				figure = {
					'data': [
						{'x': [2013, 2017], 'y': [96.7, 97.3], 'type': 'bar', 'name':'Petites'},
						{'x': [2013, 2017], 'y': [2.5, 2.0], 'type': 'bar', 'name':'Grandes'},
						{'x': [2013, 2017], 'y': [0.7, 0.7], 'type': 'bar', 'name':'Très grandes'}
					],
					'layout': {
						'title': 'Pourcentage par taille',
						'barmode':'stack'
						
					}
				}
			),

			#Graph de la répartition par région
			
			dcc.Graph(
				id = 'graph_régions',
				style = {'height': 400, 'width': 600},
				figure = {		
					'data': [
					{'x': [2013, 2017], 'y': [44.6, 44.8], 'type': 'bar', 'name':'Flandres'},
					{'x': [2013, 2017], 'y': [33.3, 33.2], 'type': 'bar', 'name':'Wallonie'},
					{'x': [2013, 2017], 'y': [22.1, 22.0], 'type': 'bar', 'name':'Bruxelles'}
					],
					'layout': {
						'title': 'Pourcentage par région',
					}
				}
			),

			

			

	], id = "first_row"),
		
		html.P('Répartition des associations et des fondations selon le statut Employeur', style = {'color':'SteelBlue', 'fontSize':20, 'textAlign':'center', 'paddingTop': 50}),

		#Graph de la répartition par statut d'employeurs par région
		#Filtrage par région
			
				html.Div([
					
					dcc.Graph(
							id = 'graph_employeurs',
							style = {'height': 400, 'width': 400},
							figure = {		
								'data': [
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [10259, 10360, 10328, 10555, 10688], 'type': 'bar', 'name':'total'},
								],
								'layout': {
									'title': "Nombres d'associations étant employeur",
									
							
								}
							}
						),
				
					
					dcc.Graph(
							id = 'graph_employeurs_régions',
							style = {'height': 400, 'width': 600},
							figure = {		
								'data': [
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [37, 36, 36, 36, 35], 'type': 'bar', 'name':'Flandres'},
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [37, 38, 38, 38, 38], 'type': 'bar', 'name':'Wallonie'},
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [25, 26, 26, 26, 27], 'type': 'bar', 'name':'Bruxelles'}
								],
								'layout': {
									'title': 'Répartition selon le statut Employeur',
									'barmode': 'stack'
								}
							}
						)
				], id = 'filtres_régions'),

		html.P('Evolution du nombre des emplois et des équivalents temps plein (ETP)', style = {'color':'SteelBlue', 'fontSize':20, 'textAlign':'center', 'paddingTop': 50}),

		html.Div([

					html.Div(),
				
					dcc.Graph(
							id = 'graph_travail',
							style = {'height': 400, 'width': 600},
							figure = {		
								'data': [
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [317643, 318956, 320695, 323864, 329642], 'type': 'bar', 'name':'Emplois'},
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [232101, 230304, 232508, 236418, 240345], 'type': 'bar', 'name':'ETP'},
								],
								'layout': {
									'title': 'Evolution des emplois et des ETP',								}
							}
						)
				], id = 'filtres_travail'),

			
		html.Div([

					html.Div(),

					dcc.Graph(
							id = 'graph_emplois_moyens',
							style = {'height': 400, 'width': 600},
							figure = {		
								'data': [
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [31.0, 30.8, 31.1, 30.7, 30.8], 'type': 'line', 'name':'Emplois'},
									{'x': [2013, 2014, 2015, 2016, 2017], 'y': [22.6, 22.2, 22.5, 22.4, 22.5], 'type': 'line', 'name':'ETP'},
								],
								'layout': {
									'title': "Nombre moyen d'emplois et d'ETP",								
								}
							}
						),

					html.Div([
						html.P('Emplois moyens:' + "\n" + str(round(m,2)), id = 'average_E', style = {'color':'white'}),

						html.P('ETP moyens:' + "\n" + str(round(n,2)), id = 'average_ETP', style = {'color':'white'})

					])
					

				], id = 'filtres_emplois_moyens'),

		html.P('Situation économique du secteur associatif en Belgique', style = {'color':'SteelBlue', 'fontSize':20, 'textAlign':'center', 'paddingTop': 50}),

		html.Div([

			html.Div(),

			dcc.Graph(
			id = 'deficit_regions',
			style = {'height':500, 'width':900},
			figure = {
				'data':[
					{'x': [2013, 2014, 2015, 2016, 2017], 'y' : [44, 37, 36, 35, 35], 'type': 'bar', 'name':'en déficit' },
					{'x': [2013, 2014, 2015, 2016, 2017], 'y' : [56, 63, 64, 65, 65], 'type': 'bar', 'name':'non déficitaire' }

				],
				'layout': {
					'title': "part des associations déficitaires et non déficitaires",
					'barmode':'stack'
				}
			}
		)

		], id = "deficit")
		


		
		
			

	], id = 'body_page'),

	
	
], id = 'main_container')


#Fonction callback pour le graph du pourcentage par région
@app.callback(
dash.dependencies.Output('graph_régions', 'figure'),
[dash.dependencies.Input('régions', 'value')])
def update_image_src(selector):		
	data = []
	if 'Flandre' in selector:
		data.append({'x': [2013, 2017], 'y': [44.6, 44.8], 'type': 'bar', 'name':'Flandres'})		
	if 'Wallonie' in selector:
		data.append({'x': [2013, 2017], 'y': [33.3, 33.2], 'type': 'bar', 'name':'Wallonie'})
	if 'Bruxelles' in selector:
		data.append({'x': [2013, 2017], 'y': [22.1, 22.0], 'type': 'bar', 'name':'Bruxelles'})
	
	figure = {
		'data': data,	
		'layout': {
			'title': 'Répartition par régions selon le statut Employeur',
			'xaxis': dict(
				title = 'Années'
			),
			'yaxis': dict(
				title = 'Pourcentage par région'
			)
			}
		}
	return figure
	


#Fonction callback pour le graph selon le statut d'employeurs
@app.callback(
dash.dependencies.Output('graph_employeurs_régions', 'figure'),
[dash.dependencies.Input('régions', 'value')])
def update_image_src(selector):		
	data = []
	if 'Flandre' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [3820, 3910, 3908, 4004, 4109], 'type': 'bar', 'name':'Flandres'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [3820, 3910, 3908, 4004, 4109], 'type': 'line', 'name':'Flandres'})		
	if 'Wallonie' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [3836, 3776, 3715, 3764, 3720], 'type': 'bar', 'name':'Wallonie'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [3836, 3776, 3715, 3764, 3720], 'type': 'line', 'name':'Wallonie'})		
	if 'Bruxelles' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [2603, 2674, 2705, 2787, 2859], 'type': 'bar', 'name':'Bruxelles'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [2603, 2674, 2705, 2787, 2859], 'type': 'line', 'name':'Bruxelles'})
	figure = {
		'data': data,	
		'layout': {
			'title': "Nombre d'associations étant employeur, par régions",
			'xaxis': dict(
				title = 'Années'
			),
			'yaxis': dict(
				title = 'Nombre par région'
			)
			}
		}
	return figure

#Fonction callback pour le graph du déficit par région
@app.callback(
dash.dependencies.Output('deficit_regions', 'figure'),
[dash.dependencies.Input('régions', 'value')])
def update_image_src(selector):		

	data = []

	if 'Flandre' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [39, 33, 31, 31, 33], 'type': 'bar', 'name':'en déficit (Fl)'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [61, 67, 69, 69, 67], 'type': 'bar', 'name':'non déficitaire (Fl)'})			
	if 'Wallonie' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [50, 40, 40, 38, 38], 'type': 'bar', 'name':'en déficit (Wl)'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [50, 60, 60, 62, 62], 'type': 'bar', 'name':'non déficitaire (Wl)'})
	if 'Bruxelles' in selector:
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [46, 41, 40, 36, 36], 'type': 'bar', 'name':'en déficit (Br)'}),
		data.append({'x': [2013, 2014, 2015, 2016, 2017], 'y': [54, 59, 60, 64, 64], 'type': 'bar', 'name':'non déficitaire (Br)'})
	
	figure = {
		'data': data,	
		'layout': {
			'title': 'Part des associations en déificit',	
			'xaxis': dict(
					title = 'Années'
				),
			'yaxis': dict(
					title = 'Pourcentage par région'
				),
			'barmode':'group'
			}
		}
	return figure
	
			
	




#Démarrage du serveur 
if(__name__ == '__main__'):
	app.run_server(debug = True)