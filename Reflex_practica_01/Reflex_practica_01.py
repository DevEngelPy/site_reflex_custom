import reflex as rx

from components.component_navbar import navbar
from components.component_footer import footer

from views.header.view_header import header
from views.links.view_links import link

#aqui se esta agrupando la maquetacion
def index()->rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        link(),
        footer()
    )

app = rx.App()
app.add_page(index)
