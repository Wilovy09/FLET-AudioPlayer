import flet as ft
from flet import *

url = r"..\music\FindeSemana.mp3"

# page.overlay.append(audio1)

def audio1():
    Audio(
    src=url,
    autoplay=True,
    volume=1,
    balance=0,
    on_loaded=lambda _: print("Loaded"),
    on_duration_changed=lambda e: print("Duration changed:", e.data),
    on_position_changed=lambda e: print("Position changed:", e.data),
    on_state_changed=lambda e: print("State changed:", e.data),
    on_seek_complete=lambda _: print("Seek complete"),
)

def volume_down(_):
    audio1.volume -= 0.1
    audio1.update()
    print(audio1.volume)

def volume_up(_):
    audio1.volume += 0.1
    audio1.update()
    print(audio1.volume)

def balance_left(_):
    audio1.balance -= 0.1
    audio1.update()
    print(audio1.balance)

def balance_right(_):
    audio1.balance += 0.1
    audio1.update()
    print(audio1.balance)

def _view_():
    return View(
        '/play_music',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda e: e.page.go('/my_music'),
                            ),
                        ]
                    ),
                    # main content
                    ft.Divider(thickness=1),
                    Container(
                        Row([
                            Column([
                                IconButton(
                                    icon=ft.icons.ADD,
                                    on_click=volume_up),
                                IconButton(
                                    icon=ft.icons.REMOVE,
                                    on_click=volume_down),
                                ]
                            ),
                            Row([
                                IconButton(
                                    icon=ft.icons.PLAY_ARROW,
                                    on_click=lambda _: audio1.resume(),
                                ),
                                IconButton(
                                    icon=ft.icons.PAUSE,
                                    on_click=lambda _: audio1.pause(),
                                ),
                                ]
                            ),                
                            Column([
                                ElevatedButton("R", on_click=balance_right),
                                ElevatedButton("L", on_click=balance_left),
                                ]
                            ),

                        ])

                    ),

                ]
            )
        ],
    )