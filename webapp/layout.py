import justpy as jp


class DefaultLayout(jp.QLayout):
    def __init__(self, view='hHh lpR fFf', **kwargs):
        super().__init__(view=view, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(
            a=self, show_if_above=True, v_mode='left', bordered=True
        )
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller, classes='p-5')
        a_classes = 'text-2xl text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Главная', href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Словарь', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(
            a=toolbar,
            dense=True,
            flat=True,
            round=True,
            icon='menu',
            click=self.move_drawer,
            drawer=drawer,
        )
        jp.QToolbarTitle(a=toolbar, text='Словарь терминов')

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
