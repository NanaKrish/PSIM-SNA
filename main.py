import os

import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

from psim.agents.entity import Population
from psim.agents.infectors import COVID19
from psim.simulator import PSIMModel
from psim.utils import helpers
cyto.load_extra_layouts()
app = dash.Dash(__name__)

CONFIG = {
    'DEBUG': True,
    'DATA_DIR': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'psim/data')
}

POPULATION_DATA_FILE = os.path.join(CONFIG['DATA_DIR'], 'population.csv')

people = helpers.load_user_data(POPULATION_DATA_FILE)
population = Population(people)

covid = COVID19(10, 10, "AirBorne")
sim = PSIMModel(population, covid)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-population-graph',
        layout={'name': 'cola'},
        style={'width': '80%', 'height': '600px'},
        elements=helpers.get_cytoscape_elts(sim.population.get_graph()),
        stylesheet=[
            {
                'selector': '[infected = "true"]',
                'style': {
                    'background-color': '#ff6e66',
                }
            },
            {
                'selector': 'node',
                'style': {
                    'label': 'data(id)',
                }
            },
            {
                'selector': '[infected = "false"]',
                'style': {
                    'background-color': '#63f2a1',
                }
            }
        ]
    ),
    html.Div([
        html.Button('Advance', id='btn-advance-next', n_clicks_timestamp=0),
    ])
])
app.title = 'PSIM'

@app.callback(Output('cytoscape-population-graph', 'elements'),
              [Input('btn-advance-next', 'n_clicks_timestamp')])
def advance(btn_advance):
    sim.simulate_one_step()
    return helpers.get_cytoscape_elts(sim.population.get_graph())


def main():
    app.run_server(debug=CONFIG['DEBUG'], use_reloader=CONFIG['DEBUG'])


if __name__ == '__main__':
    main()
