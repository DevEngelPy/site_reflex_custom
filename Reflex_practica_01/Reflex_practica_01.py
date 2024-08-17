#librera framework
import reflex as rx
 #componentes
from components.component_navbar import navbar
from components.component_footer import footer
 #vistas
from views.header.view_header import header
from views.links.view_links import link
#estilos
import styles.styles_base as styles

class State(rx.State):
    pass

#aqui se esta agrupando la maquetacion
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                link(),
                #estilos vstack
                max_width = styles.WIDTH_MAX,
                width = '100%',
                margin_y = styles.Spacer.BIG.value
            )  
        ),
        footer()
        
    )

app = rx.App()
app.add_page(index)
