from components.component_button import link_button

import reflex as rx

def link() -> rx.Component:
    return rx.vstack(
        link_button('Github','https://github.com/DevEngelPy')
    )