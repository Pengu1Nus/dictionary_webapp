import justpy as jp


class HomePage:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is HomePage page!!!', classes='text-4xl m-2')
        jp.Div(a=div, text='lorem ipsum', classes='text-lg')
        return wp
