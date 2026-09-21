only_controls = {
    "RichText.widget": """
# from database.guantanamera_db import get_database

import flet as ft


class RichText(ft.Row):

    def __init__(
        self,
        page: object=None,
        icon: object=None,
        text: str='',
        text_link: str='',
    ) -> None:
        super().__init__()
        self.page=page
        self.alignment=ft.MainAxisAlignment.START
        self.vertical_alignment=ft.CrossAxisAlignment.CENTER
        self.run_alignment=ft.CrossAxisAlignment.CENTER
        self.expand=True
        self.spacing=8
        self.run_spacing=8
        self.controls=[
            ft.Icon(name=icon),
            ft.Text(
                disabled=False,
                spans=[
                    ft.TextSpan(
                        text,
                        ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                        url=text_link,
                        on_enter=lambda data_one: self.highlight_link(
                            data_pased=data_one
                        ),
                        on_exit=lambda data_two: self.unhighlight_link(
                            data_pased=data_two
                        ),
                    ),
                ],
            ),
        ]

    def highlight_link(self,data_pased: object=None):
        data_pased.control.style.color=ft.Colors.BLUE
        data_pased.control.update()

    def unhighlight_link(self,data_pased: object=None):
        data_pased.control.style.color=None
        data_pased.control.update()

""",
    "TextSearch.widget": """
import flet as ft


class TextSearch(ft.Container):

    def __init__(
        self,
        page: object=None,
        list_filter: list=list(),
        debug: bool=False,
        padding=ft.Padding.all(8),
        go_to: str=str(),
    ) -> None:
        super().__init__()
        self.page=page
        self.debug=debug
        self.padding=padding
        self.list_filter=list_filter
        self.text_box_visible=False
        self.search_text: str=str()
        self.padding=ft.Padding.all(8)
        self.go_to=go_to
        # content of current widget
        self.content=ft.Column(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.TRANSPARENT,
                    alignment=ft.alignment.top_center,
                    padding=ft.Padding.only(left=0,right=0,bottom=0,top=0),
                    margin=ft.Margin.only(left=0,right=0,bottom=0,top=0),
                    content=ft.Container(
                        padding=ft.Padding.only(left=8,top=8,right=8,bottom=8),
                        border_radius=ft.BorderRadius.all(24),
                        expand=True,
                        bgcolor=ft.Colors.GREY900,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0,5),
                        ),
                        content=ft.Row(
                            controls=[
                                ft.TextField(
                                    expand=True,
                                    bgcolor=ft.Colors.BLACK12,
                                    label='Search',
                                    hint_text='Fill correct data',
                                    border_width=0,
                                    border_radius=ft.BorderRadius.all(18),
                                    border_color=ft.Colors.TRANSPARENT,
                                    on_change=lambda _: self.add_search(
                                        text_typed=_.data
                                    ),
                                    on_submit=lambda _: self.find_text(),
                                ),
                                ft.Container(
                                    border_radius=ft.BorderRadius.all(18),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8,
                                        color=ft.Colors.BLUE,
                                    ),
                                    padding=ft.Padding.all(8),
                                    content=ft.Icon(name='search'),
                                    on_click=lambda _: self.find_text(),
                                ),
                            ],
                        ),
                    ),
                ),
                ft.Container(
                    # expand=True,
                    visible=self.text_box_visible,
                    bgcolor=ft.Colors.TRANSPARENT,
                    alignment=ft.alignment.top_center,
                    padding=ft.Padding.only(left=0,right=0,bottom=0,top=0),
                    margin=ft.Margin.only(left=0,right=0,bottom=0,top=0),
                    content=ft.Container(
                        padding=ft.Padding.only(left=8,top=8,right=8,bottom=8),
                        border_radius=ft.BorderRadius.all(12),
                        # border_radius=ft.BorderRadius.all(24),
                        expand=True,
                        bgcolor=ft.Colors.GREY900,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0,5),
                        ),
                        content=ft.Column(
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[],
                        ),
                    ),
                ),
            ]
        )

    def visible_widget(self,visible: bool=False):
        self.content.controls[1].visible=visible

    def update_widget(self):
        self.content.controls[1].update()

    def clean_widget(self):
        self.content.controls[1].content.content.controls.clear()
        self.visible_widget(visible=False)
        self.update_widget()

    def add_search(self,text_typed: str=''):
        self.clean_widget()
        self.search_text=text_typed

    def find_text(self):
        self.clean_widget()

        for _ in self.list_filter:
            if _.startswith(self.search_text):
                self.content.controls[1].content.content.controls.append(
                    ft.ListTile(
                        # title=ft.Text(value=self.search_text),
                        title=ft.Text(value=_),
                        on_click=lambda _: self.return_text(text=_.control.title.value),
                        data=self.search_text,
                    )
                )

        if len(self.search_text) > 0:
            self.visible_widget(visible=True)
        else:
            self.visible_widget(visible=False)

        if not len(self.content.controls[1].content.content.controls) == 0:
            self.update_widget()

    def return_text(self,text: str=''):
        if self.debug:
            print(text)

        self.page.session.set('layer_one_selected',text)
        self.page.go(self.go_to)

""",
    "class_flet_simple_init": """
import flet as ft

@ft.component
def Home():
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Página de inicio"),
                ft.Button(
                    "Ir a About",
                    on_click=lambda: ft.context.page.navigate("/About"),
                ),
            ],
        ),
    )

@ft.component
def About():
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Acerca de nosotros"),
                ft.Button(
                    "Ir a Inicio",
                    on_click=lambda: ft.context.page.navigate("/"),
                ),
            ],
        ),
    )

@ft.component
def App():
    return ft.Container(
        expand=True,
        margin=ft.Margin.all(0),
        bgcolor=ft.Colors.BLACK,
        content=ft.Router([
            ft.Route(index=True, component=Home),
            ft.Route(path="About", component=About),
        ]),
    )


def main(page: ft.Page):
    # this is main function which is the entry point of the application.
    # It sets up the page properties and renders the App component.
    page.title = "Mi Aplicación Flet"
    page.theme_mode = ft.ThemeMode.DARK
    # page.bgcolor = ft.Colors.BLACK
    # page.window_width = 800
    # page.window_height = 600
    # page.window_resizable = True
    # page.window_maximizable = True
    # page.window_minimizable = True
    # page.margin = ft.Margin.all(0)
    page.padding = ft.Padding.all(0)
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.render(App)

if __name__ == "__main__":
    ft.run(lambda page: main(page),port=8081,web_renderer="canvaskit")
""",
    "class_simple_attributes": """class ${1:widget_name}(ft.Container):\n
    def __init__(self,page: ft.Control=None, content: ft.Control=None, on_click=None) -> None:
        super().__init__()
        self.page=page
        # self.tooltip='Container'
        # self.image=ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
        # self.gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.Colors.TRANSPARENT,ft.Colors.BLACK12,],)
        # self.shadow=ft.BoxShadow(spread_radius=1,blur_radius =15,color=ft.Colors.BLUEGREY_300,offset=ft.Offset(0,0),blur_style=ft.ShadowBlurStyle.OUTER,)
        # self.height=150
        # self.width=150
        # self.padding=ft.Padding.only(left=8,right=8,bottom=8,top=8)
        # self.border_radius=ft.BorderRadius.only(top_left=8,top_right=8,bottom_left=8,bottom_right=8)
        # self.border=ft.border.all(width=2,color=ft.Colors.BLACK12)
        # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
        self.alignment=ft.Alignment.CENTER
        self.expand=True
        self.ink=True
        self.bgcolor=ft.Colors(ft.Colors.BLACK12)
        self.ink_color=ft.Colors(ft.Colors.YELLOW)

        self.content=content
        self.on_click=on_click
""",
    "class_simple": """class ${1:widget_name}(ft.Container):\n
    def __init__(self,page: ft.Control=None, content: ft.Control=None, on_click=None) -> None:
        super().__init__()
        self.page=page
        self.expand=True
        self.ink=True
        self.bgcolor=ft.Colors(ft.Colors.BLACK12)
        self.ink_color=ft.Colors(ft.Colors.YELLOW)
        self.alignment=ft.Alignment.CENTER

        self.content=content
        self.on_click=on_click
""",
    "Class_test": """
import flet as ft

@ft.component
def Home():
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Página de inicio"),
                ft.Button(
                    "Ir a About",
                    on_click=lambda: ft.context.page.navigate("/About"),
                ),
            ],
        ),
    )

@ft.component
def App():
    return ft.Container(
        expand=True,
        margin=ft.Margin.all(0),
        bgcolor=ft.Colors.BLACK,
        content=ft.Router([
            ft.Route(index=True, component=Home),
        ]),
    )


def main(page: ft.Page):
    # this is main function which is the entry point of the application.
    # It sets up the page properties and renders the App component.
    page.title = "Mi Aplicación Flet"
    page.theme_mode = ft.ThemeMode.DARK
    # page.bgcolor = ft.Colors.BLACK
    # page.window_width = 800
    # page.window_height = 600
    # page.window_resizable = True
    # page.window_maximizable = True
    # page.window_minimizable = True
    # page.margin = ft.Margin.all(0)
    page.padding = ft.Padding.all(0)
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.render(App)

if __name__ == "__main__":
    ft.run(lambda page: main(page),port=8081,web_renderer="canvaskit")
    """,
    "classPage": """import flet as ft


class ${1:generic}_page(ft.Column):
    # will fix error expand widget in one screen

    def __init__(
        self,
        page: ft.Control = None,
        controls: ft.Control = None,
        on_click=None,
        bgcolor=None,
        expand=False,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=None,
    ) -> None:
        super().__init__()
        self.page = page
        self.controls = [
            ft.Container(
                alignment=ft.Alignment.CENTER,
                expand=True,
                bgcolor=bgcolor,
                content=ft.Column(
                    scroll=scroll,
                    alignment=alignment,
                    horizontal_alignment=horizontal_alignment,
                    expand=expand,
                    spacing=8,
                    run_spacing=8,
                    controls=controls,
                ),
                on_click=on_click,
            )
        ]
""",
    # FRAME CONTAINERS
    "SafeArea": """ft.SafeArea(
    expand=True,
    content=ft.Container(
        message := ft.Text("0", size=50),
        alignment=ft.Alignment.CENTER,
    ),
)""",
    "Container": """ft.Container(
    alignment=ft.Alignment.CENTER,
    expand=True,
    bgcolor=ft.Colors.BLACK12,
    content=ft.Text("flet_box"),
)""",
    "Container.attributes": """#: [rotate,offset] ,[scale,aspect_ratio] ,[visible,disabled]
    # tooltip='Container',
    # col={"md": 1}, # <= main like gridview
    # padding=ft.Padding.only(left=8,right=8,bottom=8,top=8),
    # border_radius=ft.BorderRadius.only(top_left=8,top_right=8,bottom_left=8,bottom_right=8),
    # border=ft.border.only(left=ft.border.BorderSide(8,'green'),top=None,right=None,bottom=None,),
    # border=ft.border.all(width=2,color=ft.Colors.BLACK12),
    # gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.Colors.TRANSPARENT,ft.Colors.BLACK12,],),
    # shadow=ft.BoxShadow(spread_radius=1,blur_radius =15,color=ft.Colors.BLUEGREY_300,offset=ft.Offset(0,0),blur_style=ft.ShadowBlurStyle.OUTER,),
    # image=self.image=ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02),# NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
    # height=150,
    # width=150,
    # ink=True,
    # ink_color=ft.Colors.YELLOW,
    alignment=ft.Alignment.CENTER,
    expand=True,
)""",
    "Container.extra": """ft.Container(
    #: [rotate,offset] ,[scale,aspect_ratio] ,[visible,disabled]
    # tooltip='Container',
    # col={"md": 1}, # <= main like gridview
    # padding=ft.Padding.only(left=8,right=8,bottom=8,top=8),
    # border_radius=ft.BorderRadius.only(top_left=8,top_right=8,bottom_left=8,bottom_right=8),
    # border=ft.border.only(left=ft.border.BorderSide(8,'green'),top=None,right=None,bottom=None,),
    # border=ft.border.all(width=2,color=ft.Colors.BLACK12),
    # gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.Colors.TRANSPARENT,ft.Colors.BLACK12,],),
    # shadow=ft.BoxShadow(spread_radius=1,blur_radius =15,color=ft.Colors.BLUEGREY_300,offset=ft.Offset(0,0),blur_style=ft.ShadowBlurStyle.OUTER,),
    # image=self.image=ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02),# NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
    # height=150,
    # width=150,
    # ink=True,
    # ink_color=ft.Colors.YELLOW,
    alignment=ft.Alignment.CENTER,
    expand=True,
    bgcolor=ft.Colors.BLACK12,
    content=ft.Text("flet_box"),
)""",
    "Row": """ft.Row(
    alignment=ft.MainAxisAlignment.SPACE_AROUND,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    run_alignment=ft.CrossAxisAlignment.CENTER,
    expand=True,
    spacing=8,
    run_spacing=8,
    controls=[
    ],
)""",
    "Row.attributes": """# tooltip='Row',
        # bgcolor=ft.Colors.BLACK12,
        # rotate=1,
        # offset=(0, 1),
        # scale=0.9,
        # opacity=1,
        # tight=True,
        # disabled=True,
        # wrap=True,
        # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
        # auto_scroll=True,
        # height=150,
        # width=150,
        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        run_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=8,
        run_spacing=8,
)""",
    "Row.extras": """ft.Row(
        # tooltip='Row',
        # bgcolor=ft.Colors.BLACK12,
        # rotate=1,
        # offset=(0, 1),
        # scale=0.9,
        # opacity=1,
        # tight=True,
        # disabled=True,
        # wrap=True,
        # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
        # auto_scroll=True,
        # height=150,
        # width=150,
        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        run_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=8,
        run_spacing=8,
        controls=[
            ft.MenuItemButton(
                content=ft.Text("Yes"),
                on_click=lambda e: print("yes"),
            ),
            ft.MenuItemButton(
                content=ft.Text("No"),
                on_click=lambda e: print("no"),
            ),
            ft.MenuItemButton(
                content=ft.Text("Maybe"),
                on_click=lambda e: print("maybe"),
            ),
        ],
)""",
    "Column": """ft.Column(
    alignment=ft.MainAxisAlignment.SPACE_AROUND,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    run_alignment=ft.CrossAxisAlignment.CENTER,
    expand=True,
    spacing=8,
    run_spacing=8,
    controls=[
    ],
)""",
    "Column.attributes": """# tooltip='Column',
        # bgcolor=ft.Colors.BLACK12,
        # rotate=1,
        # offset=(0,1),
        # scale=0.9,
        # opacity=1,
        # tight=True,
        # disabled=True,
        # wrap=True,
        # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
        # auto_scroll=True,
        # height=150,
        # width=150,
        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        run_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=8,
        run_spacing=8,
)""",
    "Column.extras": """ft.Column(
        # tooltip='Column',
        # bgcolor=ft.Colors.BLACK12,
        # rotate=1,
        # offset=(0,1),
        # scale=0.9,
        # opacity=1,
        # tight=True,
        # disabled=True,
        # wrap=True,
        # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
        # auto_scroll=True,
        # height=150,
        # width=150,
        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        run_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        spacing=8,
        run_spacing=8,
        controls=[
            ft.MenuItemButton(
                content=ft.Text("Yes"),
                on_click=lambda e: print("yes"),
            ),
            ft.MenuItemButton(
                content=ft.Text("No"),
                on_click=lambda e: print("no"),
            ),
            ft.MenuItemButton(
                content=ft.Text("Maybe"),
                on_click=lambda e: print("maybe"),
            ),
        ],
)""",
    "ResponsiveRow": """ft.ResponsiveRow(
    expand=True,
    # ELEMENTS IN ROW 12=1, 6=2, 4=3, 3=4, 2=6, 1=12
    # xs: small, md: medium, lg: large, xl: extra laege
    col=12, # defauld 12
    controls=[
        ft.Column(
            col={"xs": 6, "md": 3, "lg": 2},
            controls=[
                # WIDGET
            ],
        ),
        ft.Column(
            col={"xs": 6, "md": 3, "lg": 2},
            controls=[
                # WIDGET
            ],
        ),
        ft.Column(
            col={"xs": 12, "md": 12, "lg": 12},
            controls=[
                # WIDGET
            ],
        ),
    ],
),""",
    "Stack": """ft.Stack(
    width=300,
    height=300,
    controls=[
        ft.Image(
            src="https://picsum.photos/300/300",
            width=300,
            height=300,
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Image title",
                    color=ft.Colors.SURFACE_TINT,
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    opacity=0.5,
                )
            ],
        ),
    ],
)""",
    "GridView": """ft.GridView(
    controls=[
    ],
)""",
    "GridView.attributes": """expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
)""",
    "GridView.extra": """ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=[],
)""",
    # WIDGETS
    "Checkbox": """ft.Checkbox(
    height=22,
    label="flet-box",
    value=False,
    # label_position=ft.LabelPosition(),
    label_style=ft.TextStyle(
        weight=ft.FontWeight.BOLD,
        size=18,
    ),
    # OVERLINE, UNDERLINE, LINE_THROUGH,
),""",
    "AlertDialog": """ft.AlertDialog(
    modal=True,
    title=ft.Text("flet-box"),
    content=ft.Text("flet-box"),
    actions=[
        ft.TextButton(text="Yes", on_click=lambda _: print("flet-box")),
        ft.TextButton(text="No", on_click=lambda _: print("flet-box")),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
)""",
    "AnimatedSwitcher": """ft.AnimatedSwitcher(
    duration=300,
    transition=ft.AnimatedSwitcherTransition.SCALE,
    reverse_duration=100,
    switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
    switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    content=ft.Container(
        ft.Text("Hello!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.Alignment.CENTER,
        width=200,
        height=200,
        bgcolor=ft.Colors.GREEN,
    ),
)""",
    "AppBar": """ft.AppBar(
    leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("Dashboard"),
    actions=[
        ft.IconButton(ft.Icons.SEARCH),
        ft.IconButton(ft.Icons.MORE_VERT),
    ],
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
)""",
    "AutoComplete": """ft.AutoComplete(
    suggestions=[
        ("one 1", "One"),
        ("two 2", "Two"),
    ],
    on_select=lambda _: print("flet-box"),
)""",
    "AutofillGroup": """ft.AutofillGroup(
    content=ft.Column(
        controls=[
            ft.TextField(
                label="Name",
                autofill_hints=ft.AutofillHint.NAME,
            ),
            ft.TextField(
                label="Email",
                autofill_hints=[ft.AutofillHint.EMAIL],
            ),
            ft.TextField(
                label="Phone Number",
                autofill_hints=[ft.AutofillHint.TELEPHONE_NUMBER],
            ),
            ft.TextField(
                label="Street Address",
                autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,
            ),
            ft.TextField(
                label="Postal Code",
                autofill_hints=ft.AutofillHint.POSTAL_CODE,
            ),
        ]
    )
)""",
    "Badge": """ft.Icon(
    name=ft.Icons.PHONE,
    badge=ft.Badge(small_size="3"),
)""",
    "Banner": """ft.Banner(
    leading=ft.Icon(ft.Icons.INFO_OUTLINED, color=ft.Colors.PRIMARY),
    content=ft.Text("Backup completed successfully."),
    actions=[ft.TextButton("Dismiss")],
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    open=True,
)""",
    "Bottom_BottomAppBar": """ft.BottomAppBar(
    content=ft.Column(
        width=150,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Choose an option"),
            ft.TextButton("Dismiss"),
        ],
    )
)""",
    "BottomSheet": """ft.BottomSheet(
    on_dismiss=lambda _: print("flet-box"),
    content=ft.Container(
        padding=20,
        content=ft.Column(
            tight=True,
            controls=[
                ft.Text("flet-box"),
                ft.ElevatedButton(
                    "Close bottom sheet", on_click=lambda _: print("flet-box")
                ),
            ],
        ),
    ),
)""",
    "ElevatedButton": """ft.ElevatedButton(
    text="Button with colorful icon",
    icon=ft.Icons.PARK_ROUNDED,
    icon_color=ft.Colors.GREEN_400,
    on_click=lambda _: print("flet-box"),
)""",
    "CircleAvatar": """ft.CircleAvatar(
    content=ft.Text("AB"),
    bgcolor=ft.Colors.PRIMARY,
    color=ft.Colors.ON_PRIMARY,
)""",
    "Color": """ft.Colors(ft.Colors.GREY_900)""",
    "CircleAvatar": """ft.CircleAvatar(
    content=ft.Text("AB"),
    bgcolor=ft.Colors.PRIMARY,
    color=ft.Colors.ON_PRIMARY,
)""",
    "CupertinoActionSheet": """ft.CupertinoActionSheet(
    title=ft.Text("Choose an option"),
    message=ft.Text("Select what you would like to do"),
    actions=[
        ft.CupertinoActionSheetAction(content=ft.Text("Save")),
        ft.CupertinoActionSheetAction(content=ft.Text("Delete")),
    ],
    cancel=ft.CupertinoActionSheetAction(content=ft.Text("Cancel")),
)""",
    "CupertinoActivityIndicator": """ft.CupertinoActivityIndicator(
    radius=30,
    color=ft.CupertinoColors.DARK_BACKGROUND_GRAY,
)""",
    "CupertinoAlertDialog": """ft.CupertinoAlertDialog(
    title=ft.Text("Cupertino Alert Dialog"),
    content=ft.Text("Do you want to delete this file?"),
    on_dismiss=lambda _: print("flet-box"),
    actions=[
        ft.CupertinoDialogAction(
            content="Yes",
            on_click=lambda _: print("flet-box"),
        ),
        ft.CupertinoDialogAction(
            content="No", on_click=lambda _: print("flet-box")
        ),
    ],
)""",
    "CupertinoAppBar": """ft.CupertinoAppBar(
    leading=ft.Icon(ft.Icons.PALETTE, color=ft.Colors.ON_SECONDARY),
    title=ft.Text("CupertinoAppBar Example"),
    trailing=ft.Icon(ft.Icons.WB_SUNNY_OUTLINED, color=ft.Colors.ON_SECONDARY),
    automatic_background_visibility=False,
    bgcolor=ft.Colors.SECONDARY,
    brightness=ft.Brightness.LIGHT,
)""",
    "CupertinoButton": """ft.CupertinoButton(
    bgcolor=ft.CupertinoColors.LIGHT_BACKGROUND_GRAY,
    alignment=ft.alignment.top_left,
    border_radius=ft.BorderRadius.all(15),
    opacity_on_click=0.3,
    on_click=lambda e: print("Normal CupertinoButton clicked!"),
    content=ft.Text(
        value="Normal CupertinoButton",
        color=ft.CupertinoColors.DESTRUCTIVE_RED,
    ),
)""",
    "CupertinoContextMenu": """ft.CupertinoContextMenu(
    enable_haptic_feedback=True,
    content=ft.Image("https://picsum.photos/200/200"),
    actions=[
        ft.CupertinoContextMenuAction(
            content="Action 1",
            trailing_icon=ft.Icons.CHECK,
            on_click=lambda e: print("Action 1"),
        ),
        ft.CupertinoContextMenuAction(
            content="Action 2",
            trailing_icon=ft.Icons.MORE,
            on_click=lambda e: print("Action 2"),
        ),
        ft.CupertinoContextMenuAction(
            content="Action 3",
            trailing_icon=ft.Icons.CANCEL,
            on_click=lambda e: print("Action 3"),
        ),
    ],
)""",
    "CupertinoDatePicker": """ft.CupertinoDatePicker(
    value=datetime.datetime.now(),
    date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
    on_change=lambda e: print("Normal CupertinoButton clicked!"),
)""",
    "CupertinoFilledButton": """ft.CupertinoFilledButton(
    content=ft.Text("CupertinoFilledButton"),
    opacity_on_click=0.3,
    on_click=lambda e: print("CupertinoFilledButton clicked!"),
)""",
    "CupertinoListTile": """ft.CupertinoListTile(
    notched=True,
    additional_info=ft.Text("Thu Jan 25"),
    leading=ft.Icon(ft.CupertinoIcons.GAME_CONTROLLER),
    title=ft.Text("CupertinoListTile: notched=True"),
    subtitle=ft.Text("Subtitle"),
    trailing=ft.Icon(ft.CupertinoIcons.ALARM),
    on_click=lambda e: print("Action 3"),
)""",
    "CupertinoNavigationBar": """ft.CupertinoNavigationBar(
    bgcolor=ft.Colors.AMBER_100,
    inactive_color=ft.Colors.GREY,
    active_color=ft.Colors.BLACK,
    on_change=lambda e: print("Selected tab:", e.control.selected_index),
    destinations=[
        ft.NavigationBarDestination(
            icon=ft.Icons.EXPLORE_OUTLINED,
            selected_icon=ft.Icons.EXPLORE,
            label="Explore",
        ),
        ft.NavigationBarDestination(
            icon=ft.Icons.COMMUTE_OUTLINED,
            selected_icon=ft.Icons.COMMUTE,
            label="Commute",
        ),
        ft.NavigationBarDestination(
            icon=ft.Icons.BOOKMARK_BORDER,
            selected_icon=ft.Icons.BOOKMARK,
            label="Favorites",
        ),
    ],
)""",
    "CupertinoPicker": """ft.CupertinoPicker(
    selected_index=3,
    magnification=1.22,
    squeeze=1.2,
    use_magnifier=True,
    on_change=lambda e: print("CupertinoFilledButton clicked!"),
    controls=[
        ft.Text(value=f)
        for f in [
            "Apple",
            "Mango",
            "Banana",
            "Orange",
            "Pineapple",
            "Strawberry",
        ]
    ],
)""",
    "RadioGroup": """ft.RadioGroup(
    value="option_2",
    content=ft.Column(
        controls=[
            ft.CupertinoRadio(value="option_1", label="Option 1"),
            ft.CupertinoRadio(value="option_2", label="Option 2"),
            ft.CupertinoRadio(value="option_3", label="Option 3"),
        ],
    ),
)""",
    "CupertinoSegmentedButton": """ft.CupertinoSegmentedButton(
    controls=[
        ft.Text("One"),
        ft.Text("Two"),
        ft.Text("Three"),
    ],
    selected_index=1,
)""",
    "CupertinoSlider": """ft.CupertinoSlider(
    divisions=20,
    min=0,
    max=100,
    active_color=ft.Colors.PURPLE,
    thumb_color=ft.Colors.PURPLE,
    on_change_start=lambda _: print("flet-box"),
    on_change_end=lambda _: print("flet-box"),
    on_change=lambda _: print("flet-box"),
)""",
    "CupertinoSlidingSegmentedButton": """ft.CupertinoSlidingSegmentedButton(
    selected_index=1,
    controls=[
        ft.Text("One"),
        ft.Text("Two"),
        ft.Text("Three"),
    ],
)""",
    "CupertinoSwitch": """ft.CupertinoSwitch(
    label="Cupertino Switch",
    value=True,
)""",
    "CupertinoTextField": """ft.CupertinoTextField(
    value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    multiline=True,
    min_lines=3,
    autofocus=True,
    on_click=lambda _: print("flet-box"),
)""",
    "CupertinoTimerPicker": """ft.CupertinoTimerPicker(
    value=300,
    second_interval=10,
    minute_interval=1,
    mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
    on_change=lambda _: print("flet-box"),
)""",
    "DatePicker": """ft.DatePicker(
    first_date=datetime.datetime(year=2024 - 1, month=1, day=1),
    last_date=datetime.datetime(year=2025 + 1, month=8, day=20),
    on_change=lambda _: print("flet-box"),
    on_dismiss=lambda _: print("flet-box"),
)""",
    "DataTable": """ft.DataTable(
    columns=[
        ft.DataColumn(label=ft.Text("Name")),
        ft.DataColumn(label=ft.Text("Role")),
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("Alice")),
                ft.DataCell(ft.Text("Engineer")),
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("Bob")),
                ft.DataCell(ft.Text("Designer")),
            ]
        ),
    ],
)""",
    "DataRow": """ft.DataRow(
    cells=[
        ft.DataCell(ft.Text("Bob")),
        ft.DataCell(ft.Text("Designer")),
    ]
)""",
    "Dismissible": """ft.Dismissible(
    content=ft.ListTile(title=ft.Text("Item ")),
    dismiss_direction=ft.DismissDirection.HORIZONTAL,
    background=ft.Container(bgcolor=ft.Colors.GREEN),
    secondary_background=ft.Container(bgcolor=ft.Colors.RED),
    on_dismiss=lambda _: print("flet-box"),
    on_confirm_dismiss=lambda _: print("flet-box"),
    on_update=lambda _: print("flet-box"),
    dismiss_thresholds={
        ft.DismissDirection.END_TO_START: 0.2,
        ft.DismissDirection.START_TO_END: 0.2,
    },
)""",
    "Divider": """ft.Divider(
    height=1,
    color=ft.Colors.WHITE,
)""",
    "Dropdown": """ft.Dropdown(
    color=ft.Colors.GREY_300,
    filled=True,
    expand=True,
    fill_color=ft.Colors.BLACK12,
    border_radius=ft.BorderRadius.all(18),
    border=ft.InputBorder.UNDERLINE,
    enable_filter=True,
    editable=True,
    leading_icon=ft.Icons.SEARCH,
    label="Icon",
    options=[
        ft.DropdownOption(key=icon["name"], leading_icon=icon["icon"])
        for icon in [
            {"name": "Smile", "icon": ft.Icons.SENTIMENT_SATISFIED_OUTLINED},
            {"name": "Cloud", "icon": ft.Icons.CLOUD_OUTLINED},
            {"name": "Brush", "icon": ft.Icons.BRUSH_OUTLINED},
            {"name": "Heart", "icon": ft.Icons.FAVORITE},
        ]
    ],
)""",
    "DropdownM2": """ft.DropdownM2(
    width=100,
    value="Green",
    options=[
        ft.dropdownm2.Option("Red"),
        ft.dropdownm2.Option("Green"),
        ft.dropdownm2.Option("Blue"),
    ],
)""",
    "ExpansionPanelList": """ft.ExpansionPanelList(
    width=400,
    controls=[
        ft.ExpansionPanel(
            header=ft.Text("Shipping address"),
            content=ft.Text("123 Market Street, Springfield"),
            expanded=True,
        ),
        ft.ExpansionPanel(
            header=ft.Text("Billing address"),
            content=ft.Text("Same as shipping"),
        ),
    ],
)""",
    "ExpansionTile": """ft.ExpansionTile(
    width=400,
    title="Account",
    subtitle="Manage profile and security",
    # expanded=True,
    controls=[
        ft.ListTile(title=ft.Text("Profile")),
        ft.ListTile(title=ft.Text("Security")),
    ],
)""",
    "FilledButton": """ft.FilledButton(
    text="Button with icon", icon=ft.Icons.ADD_OUTLINED
)""",
    "FilledTonalButton": """ft.FilledTonalButton(
    text="Button with icon",
    icon=ft.Icons.ADD_OUTLINED,
    on_click=lambda _: print("flet-box"),
)""",
    "FloatingActionButton": """ft.FloatingActionButton(
    icon=ft.Icons.ADD,
    bgcolor=ft.Colors.LIME_300,
    on_click=lambda _: print("flet-box"),
)""",
    "GestureDetector": """ft.GestureDetector(
    content=ft.Container(bgcolor=ft.Colors.GREEN, width=200, height=200),
    hover_interval=50,
    on_tap=lambda e: print(e),
    on_tap_down=lambda e: print(e),
    on_tap_up=lambda e: print(e),
    on_secondary_tap=lambda e: print(e),
    on_secondary_tap_down=lambda e: print(e),
    on_secondary_tap_up=lambda e: print(e),
    on_long_press_start=lambda e: print(e),
    on_long_press_end=lambda e: print(e),
    on_secondary_long_press_start=lambda e: print(e),
    on_secondary_long_press_end=lambda e: print(e),
    on_double_tap=lambda e: print(e),
    on_double_tap_down=lambda e: print(e),
    on_pan_start=lambda e: print(e),
    on_pan_update=lambda e: print(e),
    on_pan_end=lambda e: print(e),
    on_hover=lambda e: print(e),
    on_enter=lambda e: print(e),
    on_exit=lambda e: print(e),
)""",
    "Icon": """ft.Icon(
    name=ft.Icon(ft.Icons.MENU),
    color=ft.Colors.GREEN_400,
    size=30,
)""",
    "IconButton": """ft.IconButton(
    icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED,
    data=0,
    on_click=lambda _: print("flet-box"),
)""",
    "Image": """ft.Image(
    src="https://flet.dev/img/logo.svg",
    width=100,
    height=100,
)""",
    "InteractiveViewer": """ft.InteractiveViewer(
    min_scale=0.1,
    max_scale=15,
    boundary_margin=ft.Margin.all(20),
    on_interaction_start=lambda e: print(e),
    on_interaction_end=lambda e: print(e),
    on_interaction_update=lambda e: print(e),
    content=ft.Image(
        src="https://picsum.photos/500/500",
    ),
)""",
    "ListTile": """ft.ListTile(
    leading=ft.Icon(ft.Icons.SNOOZE),
    title=ft.Text(value="Two-line with leading and trailing controls"),
    subtitle=ft.Text("Here is a second title."),
    trailing=ft.PopupMenuButton(
        icon=ft.Icons.MORE_VERT,
        items=[
            ft.PopupMenuItem(content="Item 1"),
            ft.PopupMenuItem(content="Item 2"),
        ],
    ),
)""",
    "ListView": """ft.ListView(
    spacing=10,
    padding=20,
    width=150,
    auto_scroll=True,
    controls=[
        ft.Text(f"Line {i}", color=ft.Colors.ON_SECONDARY) for i in range(0, 60)
    ],
)""",
    "Markdown": """ft.Markdown(
    value="# Welcome\n\nThis is **Markdown** rendered in Flet.",
    width=260,
    selectable=True,
    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
    on_tap_link=lambda e: print(e),
)""",
    "MenuBar": """"""
    """ft.MenuBar(
    controls=[
        ft.SubmenuButton(
            content=ft.Text("Submenu"),
            controls=[
                ft.MenuItemButton(content=ft.Text("Item 1")),
                ft.MenuItemButton(content=ft.Text("Item 2")),
                ft.MenuItemButton(content=ft.Text("Item 3")),
            ],
        ),
    ],
)""",
    "SearchBar": """ft.SearchBar(
    view_elevation=4,
    divider_color=ft.Colors.AMBER,
    bar_hint_text="Search colors...",
    view_hint_text="Choose a color from the suggestions...",
    on_change=lambda e: print("maybe"),
    on_submit=lambda e: print("maybe"),
    on_tap=lambda e: print("maybe"),
    controls=[
        ft.ListTile(
            title=ft.Text(item),
            data=item,
            on_click=lambda e: print("maybe"),
        )
        for item in [
            "Amber",
            "Blue Grey",
            "Brown",
            "Deep Orange",
            "Green",
            "Light Blue",
            "Orange",
            "Red",
        ]
    ],
)""",
    "SegmentedButton": """ft.SegmentedButton(
    on_change=lambda e: print("maybe"),
    selected_icon=ft.Icon(ft.Icons.CHECK_SHARP),
    selected=["1", "4"],
    allow_empty_selection=True,
    allow_multiple_selection=True,
    segments=[
        ft.Segment(
            value="1",
            label=ft.Text("One"),
            icon=ft.Icon(ft.Icons.LOOKS_ONE),
        ),
        ft.Segment(
            value="2",
            label=ft.Text("Two"),
            icon=ft.Icon(ft.Icons.LOOKS_TWO),
        ),
        ft.Segment(
            value="3",
            label=ft.Text("Three"),
            icon=ft.Icon(ft.Icons.LOOKS_3),
        ),
        ft.Segment(
            value="4",
            label=ft.Text("Four"),
            icon=ft.Icon(ft.Icons.LOOKS_4),
        ),
    ],
)""",
    "Segment": """ft.Segment(
    value="4",
    label=ft.Text("Four"),
    icon=ft.Icon(ft.Icons.LOOKS_4),
)""",
    "SelectionArea": """ft.SelectionArea(
    content=ft.Column(
        controls=[
            ft.Text(
                "Selectable text",
                color=ft.Colors.GREEN,
                style=ft.TextStyle(
                    size=22,
                    weight=ft.FontWeight.W_600,
                    decoration=ft.TextDecoration(
                        ft.TextDecoration.UNDERLINE | ft.TextDecoration.OVERLINE
                    ),
                    decoration_style=ft.TextDecorationStyle.WAVY,
                ),
                key="selectable",
            ),
            ft.Text(
                "Also selectable",
                color=ft.Colors.GREEN,
                style=ft.TextStyle(
                    size=22,
                    weight=ft.FontWeight.W_600,
                    decoration=ft.TextDecoration(
                        ft.TextDecoration.UNDERLINE | ft.TextDecoration.OVERLINE
                    ),
                    decoration_style=ft.TextDecorationStyle.WAVY,
                ),
            ),
        ]
    )
)""",
    "Semantics": """ft.Semantics(
    label="Input your occupation",
    on_did_gain_accessibility_focus=lambda _: _(ft.Event[ft.Semantics]),
    on_did_lose_accessibility_focus=lambda _: _(ft.Event[ft.Semantics]),
    content=ft.TextField(
        label="Occupation",
        hint_text="Use 20 words or less",
        value="What is your occupation?",
    ),
)""",
    "ShaderMask": """ft.ShaderMask(
    blend_mode=ft.BlendMode.MULTIPLY,
    shader=ft.RadialGradient(
        center=ft.Alignment.CENTER,
        radius=0.5,
        colors=[ft.Colors.WHITE, ft.Colors.PINK],
        tile_mode=ft.GradientTileMode.CLAMP,
    ),
    content=ft.Image(
        src="https://picsum.photos/id/288/300/300",
        width=300,
        height=300,
    ),
)""",
    "Slider": """ft.Slider(
    min=100,
    max=900,
    divisions=8,
    label="Weight={value}",
    width=500,
    on_change=lambda e: print("Custom Undo clicked"),
)""",
    "SubmenuButton": """ft.SubmenuButton(
    content=ft.Text("Choose text style"),
    key="smbutton",
    expand=True,
    menu_style=ft.MenuStyle(
        alignment=ft.alignment.bottom_left, side=ft.BorderSide(1)
    ),
    controls=[
        ft.MenuItemButton(
            content=ft.Text("Underlined"),
            on_click=lambda e: print(f"{e.control.content.value}.on_click"),
        ),
    ],
)""",
    "Switch": """ft.Switch(
    label="Light ThemeMode",
    on_change=lambda e: print(f"{e.control.content.value}.on_click"),
)""",
    "Tabs": """ft.Tabs(
    height=700,
    selected_index=0,
    animation_duration=300,
    adaptive=True,
    tabs=[
        ft.Tab(
            text="Buy Order",
            content=ft.Container(
                blur=(15, 12),
                padding=ft.Padding.all(0),
                margin=ft.Margin.all(0),
                # bgcolor=ft.Colors.BLACK38,
                content=ft.Column(
                    # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                    controls=[
                        ft.Text(value="Tab 1"),
                    ]
                ),
                alignment=ft.alignment.top_left,
            ),
        ),
        ft.Tab(
            text="Sell Order",
            content=ft.Container(
                blur=(15, 12),
                content=ft.Column(
                    # scroll=ft.ScrollMode.HIDDEN,# ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                    controls=[
                        ft.Text(value="Tab 2"),
                    ]
                ),
                alignment=ft.alignment.top_left,
            ),
        ),
    ],
    expand=1,
)""",
    "Text": """ft.Text(
    # semantics_label='Double dollars',
    # tooltip='Text',
    # style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ),# OVERLINE, UNDERLINE, LINE_THROUGH
    # color=ft.Colors.BLACK12,
    # bgcolor=ft.Colors.BLACK12,
    # aspect_ratio=1,
    # rotate=1,
    # offset=(0, 1),
    # scale=0.9,
    # opacity=1,
    # visible=False,
    # max_lines=1,
    # overflow='ellipsis',
    # spans=[ft.TextSpan('here goes italic', ft.TextStyle(italic=True, size=20, color=ft.Colors.BLUE),),],
    # height=150,
    # width=150,
    # disabled=True,
    # selectable=True,
    # italic=True,
    theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
    size=12,
    expand=True,
    value="Hello World",
    text_align=ft.TextAlign.CENTER,
    weight=ft.FontWeight.BOLD,
    font_family="Consolas",
)""",
    "TextButton": """ft.TextButton(
    key="TextButton",
    data=0,
    icon=ft.Icons.PARK_ROUNDED,
    icon_color=ft.Colors.GREEN_400,
    content=ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5,
        controls=[
            ft.Text(value="Compound button", size=20),
            ft.Text(value="This is secondary text"),
        ],
    ),
    on_click=lambda e: print("Custom Undo clicked"),
)""",
    "TextField": """ft.TextField(
    expand=True,
    bgcolor="black12",
    label="Search",
    hint_text="Fill correct data",
    border_width=0,
    border_radius=ft.BorderRadius.all(18),
    border_color=ft.Colors.TRANSPARENT,
)""",
    "ShakeDetector": """ft.ShakeDetector(
    minimum_shake_count=2,
    shake_slop_time_ms=300,
    shake_count_reset_time_ms=1000,
    on_shake=lambda _: page.add(ft.Text("Shake detected!")),
) """,
    "TimePicker": """ft.TimePicker(
    # value="19:30",
    confirm_text="Confirm",
    error_invalid_text="Time out of range",
    help_text="Pick your time slot",
    on_change=lambda e: print("Custom Undo clicked"),
    on_dismiss=lambda e: print("Custom Undo clicked"),
    on_entry_mode_change=lambda e: print("Custom Undo clicked"),
)""",
    "TransparentPointer": """ft.TransparentPointer(
    content=ft.Container(
        content=ft.Button(
            "Test button",
            on_click=lambda e: print("Custom Undo clicked"),
        ),
        padding=50,
    )
)""",
    "VerticalDivider": """ft.VerticalDivider(width=1, color=ft.Colors.WHITE, thickness=3)""",
    "scaffold.Appbar": """AppBar(
        page=self.page,
        # backgroundColor=theme_codex.get(\"bg_appbar\"),
        # MENU ICON LEFT
        leading=ft.Icon(
            name=ft.Icons.BARCODE_READER,
            # color=theme_codex.get(\"primary_button_bg\"),
        ),
        # BAR TITLE
        title=ft.Text(
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            size=28,
            # expand=True,
            value=\"Flet-box\",
            # color=theme_codex.get(\"primary_button_bg\"),
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
            font_family=\"Consolas\",
        ),
        actions=[
            # MENU ICON RIGHT
            ft.IconButton(
                # icon_color=theme_codex.get(\"primary_button_bg\"),
                icon=ft.Icons.TABLE_ROWS_ROUNDED,
                # icon=ft.Icons.NOW_WIDGETS_ROUNDED,
                on_click=lambda _: self.page.open(
                    _.control.parent.parent.drawer,
                ),
            )
        ],
    ),""",
    "scaffold.structure.model": """ Scaffold(
    page=self.page,
    route=self.route,
    # HEADER
    appbar=None,
    drawer=None,
    # CONTENT
    body=[],
    # FOOTER
    bottonNavigationBar=None,
    floatingActionButton=None,
)
""",
    "scaffold.floatingActionButton": """ FloatingActionButton(
   foregroundColor=ft.Colors(ft.Colors.GREY_300),
   backgroundColor=ft.Colors(ft.Colors.GREY_900),
   mini=False,
   disableElevation=False,
   focusElevation=0,
   child=ft.Icons.ADD,
   onPressed=lambda _: print(_.control),
)
""",
    "scaffold.Drawer.Custom": """CustomDrawer(
        page=self.page,
        banner="banner.png",
    ),
                  """,
    "scaffold.Drawer": """ Drawer(
    page=self.page,
    controls=[
        # IMAGE HEADER
        ft.Container(
            height=230,
            bgcolor=ft.Colors.GREY_900,
            alignment=ft.Alignment.CENTER,
            content=ft.Text(value="Avatar"),
        ),
        # TEXT HEADER
        ft.Divider(thickness=0.1),
        ft.Container(
            alignment=ft.Alignment.CENTER,
            content=ft.Text(
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
                value="MENU SETTINGS",
            ),
        ),
        ft.Divider(thickness=0.1),
        # BODY
        ft.NavigationDrawerDestination(
            label="Version App",
            bgcolor=ft.Colors.TRANSPARENT,
            icon=ft.Icons.UPDATE,
            selected_icon=ft.Icons.MOVE_UP_ROUNDED,
        ),
        ft.Divider(thickness=0.1),
        # SPACCING ITS NNECESSARY TO PUT
        # EXACTLY POSITION
        ft.Container(height=340),
    ],
    # TEXT FOOTER
    footer_bar=ft.Container(
        padding=ft.Padding.all(8),
        bgcolor=ft.Colors.GREY_900,
        content=ft.Text(
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
            font_family="Consolas",
            value="© All right reserved @kuko54448",
        ),
    ),
    # on_click=lambda _: print(_.control.selected_index),
    on_click=lambda _: print(_.control),
)
""",
    "scaffold.BottomNavigationBar": """ BottomNavigationBar(
    page=self.page,
    backgroundColor=ft.Colors(ft.Colors.GREY_900),
    shape=ft.NotchShape.CIRCULAR,
    items=[
        BottomNavigationBarItem(
            page=self.page,
            icon=ft.Icon(ft.Icons.GROUP),
            label="GROUP",
        ),
        BottomNavigationBarItem(
            page=self.page,
            icon=ft.Icon(ft.Icons.MARKUNREAD_MAILBOX_ROUNDED),
            label="iNBOX",
        ),
        BottomNavigationBarItem(
            page=self.page,
            icon=ft.Icon(ft.Icons.NOTIFICATIONS_ACTIVE),
            label="NOTIFICATION",
        ),
    ],
    # ontab=lambda _: print(_.control.parent.controls,_.control.selectedindex),
    ontab=lambda _: _.control.parent.screen_manager(
        current_index=_.control.selected_index,
        # screens=screens,
        screens=_.control.parent.controls,
        parent_widget=_.control.parent,
    ),
)
""",
    "alertDialog.Confirmationr": """
class AlertDialogConfirmation(ft.AlertDialog):

    def __init__(self,
             page: object=None,
             header_text='Please confirm',
             body_text: str='Do you really want to delete all those files?',
             ) -> None:
        super().__init__()
        self.page=page

        self.scrollable=True,
        self.content_padding=ft.Padding.all(8),
        self.inset_padding=ft.Padding.all(12),

        self.modal=True
        self.title=ft.Text(header_text)
        self.content=ft.Text(body_text)
        self.actions=[
            ft.TextButton('Yes',
                          on_click=lambda e:self.confirm_yes(self)
                          ),
            ft.TextButton('No',
                          on_click=lambda e:self.handle_close(self)
                          ),
        ]
        self.actions_alignment=ft.MainAxisAlignment.END
        self.on_dismiss=lambda e:self.page.add(ft.Text('Non-modal dialog dismissed'))

    def handle_close(self,e):
        # self.page.open(alert)
        self.page.close(e)
    
    def confirm_yes(self,e):
        print('<<<<')
""",
}

if __name__ == "__main__":
    import flet as ft

    snippets = [_ for _ in only_controls.keys()]
    widgets = [
        n for n in dir(ft) if not n.startswith("_") and type(getattr(ft, n)) == type
    ]
    current_dictionary = {}
    no_appear = {}

    for _ in widgets:
        if _ in snippets:
            current_dictionary[_] = f"""{only_controls.get(_)}"""
        else:
            current_dictionary[_] = ""

    with open("snippets.py", "w") as f:
        f.writelines(f"data = {current_dictionary}")

    # with open("snippets2.py", "w") as f:
    #     f.writelines(f"data = {no_appear}")

    # print(current_dictionary.keys())
    # for _ in widgets:
    #     print(f'{_}:'ft.{_}()',')
    # print(widgets)
    # print("E", snippets)
