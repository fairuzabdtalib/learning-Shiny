from shiny import App, ui

app_ui = ui.page_navbar(  
    ui.nav_panel("Sales", 
        ui.layout_sidebar(
            ui.sidebar(
                
                ui.input_file("sales_csv", "Upload Actual Sales (csv)", accept=[".csv"]),
                ui.input_date_range("date_sales", "Model training period", start="2020-09-01", end="2024-06-30", format="M yyyy"),
                ui.input_numeric("sales_forecast_horizon", "Forecast horizon", value=6),
                ui.input_action_button("run_sales_model", "Run model"),
                ui.input_action_button("export_sales_forecast", "Export forecast")
                
            ),
            
        )
    ),  
    ui.nav_panel("Generation", 
        ui.layout_sidebar(
            ui.sidebar(
                
                ui.input_file("generation_csv", "Upload Actual Gen (csv)", accept=[".csv"]),
                ui.input_date_range("date_generation", "Model training period", start="1978-01-01", end="2024-06-30", format="M yyyy"),
                ui.input_numeric("generation_forecast_horizon", "Forecast horizon", value=6),
                ui.input_action_button("run_generation_model", "Run model"),
                ui.input_action_button("export_generation_forecast", "Export forecast")
                
            ),
            
        )
    ),
    title="ICPT Demand Forecast Dashboard",  
    id="navbar",
    fillable=True,
)  


def server(input, output, session):
    pass


app = App(app_ui, server)