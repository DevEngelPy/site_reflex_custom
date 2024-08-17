import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.link(
            f'2021-{datetime.date.today().year} DEVEGELPY',
            href='https://github.com/DevEngelPy',
            is_external=True
        ),
        rx.text('Dev FullStack')
    )