import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        #propiedades del texto
        rx.text('DevEngelPy', height = '40px'),
        #propiedades que se le estandando al hstack
        position = 'sticky',  
        bg = 'blue',
        padding_x = '16px',
        padding_y = '8px',
        z_index = '999'
    )