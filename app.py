from shiny import App, ui

app_ui = ui.page_navbar(  
    ui.nav_panel("Sales", 
        ui.layout_sidebar(
            ui.sidebar(
                ui.h3("Sales Input", style="font-size: 1.0em;"),
                ui.input_date_range("date_sales", "Date Range", start="2024-01-01", end="2024-01-31"),
                ui.input_select("product_sales", "Product", choices=["Product A", "Product B", "Product C"]),
            ),
            ui.output_text("content_sales"),
        )
    ),  
    ui.nav_panel("Generation", 
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_date_range("date_generation", "Date Range", start="2024-01-01", end="2024-01-31"),
                ui.input_select("product_generation", "Product", choices=["Product A", "Product B", "Product C"]),
            ),
            ui.output_text("content_generation"),
        )
    ),
    title="ICPT Demand Forecast Dashboard",  
    id="navbar",
    fillable=True,
)  


def server(input, output, session):
    pass


app = App(app_ui, server)


# import matplotlib.pyplot as plt
# import numpy as np

# from shiny import App, Inputs, Outputs, Session, render, ui

# app_ui = ui.page_fluid(
#     ui.layout_sidebar(
#         ui.sidebar(
#             ui.input_slider("n", "N", min=0, max=100, value=20),
#         ),
#         ui.output_plot("plot"),
#     ),
# )


# def server(input: Inputs, output: Outputs, session: Session):
#     @render.plot(alt="A histogram")
#     def plot() -> object:
#         np.random.seed(19680801)
#         x = 100 + 15 * np.random.randn(437)

#         fig, ax = plt.subplots()
#         ax.hist(x, input.n(), density=True)
#         return fig


# app = App(app_ui, server)