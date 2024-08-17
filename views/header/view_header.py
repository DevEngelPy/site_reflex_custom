import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='DevEngelPy', size='xl'),
        rx.text('@EngelDark'),
        rx.text('Mi Nombre Es Angel')
    )