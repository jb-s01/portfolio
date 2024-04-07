import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Data Assets
df_resume = pd.read_csv(r'/Users/jbslaunwhite01/projects/portfolio/resume.csv')

# External stylesheets (e.g., Bootstrap)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Define the layout of the app
app.layout = html.Div([
    html.H1(children='Jonas Slaunwhite', style={'textAlign':'center'}),
    html.P(children='Professional Portfolio', style={'textAlign':'center'}),
    # Add a container to hold the content of the entire single-page report
    dbc.Container([
        html.Section(id='bio', children=[
            html.H1("Biography"),
            html.P(children="""My name is Jonas Slaunwhite, from Halifax, Nova Scotia. I'm a warm-hearted professional who takes pride in my extensive experience within the financial services, alternative investment, and consulting sectors. As a dedicated leader, I enjoy collaborating with diverse teams to create meaningful change and drive success. 
                   \n My expertise lies in data analytics, business analysis, and business transformation, along with project management, financial asset valuation, derivative investment valuation, and risk management. I hold an undergraduate degree with a focus on Accounting from St. Mary's University, which has laid the foundation for my continued growth.
                   \n I am a self-taught python developer, starting in 2016 with three years of professional development experience and I continue to work on expanding my knowledge in data analytics, application development and web applications.
                   """),
            # Content for Biography
        ]),
        html.Hr(),  # Add horizontal line for separation
        html.Section(id='skills', children=[
            html.H1("Skills"),
            html.P(children="Python Data Analytics & Software Engineering"),
            html.P(children="Big Data Analytics with Apache Spark"),
            html.P(children="Business Analysis with SQL"),
            html.P(children="Advanced Applied Finance & Accounting"),
            html.P(children="Project Management & Engagement Leadership"),
            # Content for Skills
        ]),
        html.Hr(),
        html.Section(id='resume', children=[
            html.H1("Resume"),
            dash_table.DataTable(data=df_resume.to_dict('records'), page_size=10),
            
        ]),
        html.Hr(),
        html.Section(id='projects', children=[
            html.H1("Education"),
            html.P(children="Saint Mary's University - Bachelor of Commerce, Accounting (2012)"),
            
        ]),
        html.Hr(),
        html.Section(id='projects', children=[
            html.H1("Projects"),
            # Content for Projects
        ]),
        html.Hr(),
        html.Section(id='contact', children=[
            html.H1("Contact"),
            html.P(children="LinkedIn: https://www.linkedin.com/in/jbslaunwhite/"),
            html.P(children="GitHub: https://github.com/jb-s01"),
            # Content for Contact
        ]),
    ], fluid=True)
])

if __name__ == '__main__':
    app.run_server(debug=True)
