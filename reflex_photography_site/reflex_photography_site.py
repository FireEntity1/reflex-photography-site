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
            rx.heading("FireEntity's Aviation Photography", size="9"),
            rx.divider(width="100%",margin_bottom="5%",margin_top="5%"),
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
                style={
        "box-shadow": "0 0 15px 5px rgba(0, 123, 255, 0.4)",
    },),
                initial={"scale": 0.9},
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
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(255, 50, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-02.jpg",is_external=True),margin_bottom="5%",
            ),
            
            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-04.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("Air Canada 737 Max 8",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(255, 50, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-04.jpg",is_external=True),margin_bottom="5%",
            ),

        rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-03.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("WestJet 737 Max 8",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(0, 150, 150, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-03.jpg",is_external=True),margin_bottom="5%",
            ),

        rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/KLM-OP-2.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("KLM 777-300 Orange Pride",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(250, 100, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/KLM-OP-2.jpg",is_external=True),margin_bottom="5%",
            ),

            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/KLM-OP-3.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("KLM 777-300 Orange Pride",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(250, 100, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/KLM-OP-3.jpg",is_external=True),margin_bottom="5%",
            ),

        rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/KLM-OP-1.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("KLM 777-300 Orange Pride",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(250, 100, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/KLM-OP-1.jpg",is_external=True),margin_bottom="5%",
            ),

            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-07.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("Air Canada 787-8",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(250, 0, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-07.jpg",is_external=True),margin_bottom="5%",
            ),

            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-06.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("WestJet Link Saab 340b",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(0, 250, 100, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-06.jpg",is_external=True),margin_bottom="5%",
            ),

            rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-09.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("Flair 737 Max 8",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(0, 200, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-09.jpg",is_external=True),margin_bottom="5%",
            ),

        rx.center(rx.link(
                motion(
                rx.card(
                    rx.inset(
                        rx.image(
                            src="/Aug11-08.jpg",
                            width="90vw",
                            height="auto",
                        ),
                        side="top",
                        pb="current",
                    ),
                    rx.center(
                    rx.code("Flair 737 Max 8",size="6"),
                    width="100%",),style={
        "box-shadow": "0 0 15px 5px rgba(0, 200, 0, 0.5)",
    },
                size="4",flex_grow="5"
                ),
                initial={"scale": 0.9},
                while_hover={"scale": 1.1, "rotate": 5,"translate": {50,50,50}},
                while_tap={"scale": 1.3},
                transition={"type": "spring", "stiffness": 500, "damping": 25,},
            ),href="/Aug11-08.jpg",is_external=True),margin_bottom="5%",
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
