"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_motion import motion
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("FireEntity's Aviation Photography", size="9"),rx.divider(width="100%",margin_bottom="5%",margin_top="10%"),
            rx.text(
                "A collection of photos I've taken over the months!",
                size="5",margin_bottom="8%",
            ),
            rx.flex(

                rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-01.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("KLM 777-200",size="6"),
                    width="100%",),
                ),
                initial={"scale": 1},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-01.jpg",is_external=True),margin_bottom="5%",
            ),
            
            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-02.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("Air Canada Express Dash-8",size="6"),
                    width="100%",),
                size="4",flex_grow="5"
                ),
                initial={"scale": 1},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-02.jpg",is_external=True),margin_bottom="5%",
            ),
            
            spacing="5",
            flex_wrap="wrap",
            width="100%",
            ),
            justify="center",
            min_height="85vh",
            
        ),
    )


app = rx.App()
app.add_page(index)
