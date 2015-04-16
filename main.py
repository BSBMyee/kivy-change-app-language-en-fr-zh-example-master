from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from os.path import join, dirname
import gettext


class MySpecialLabel(Label):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.app.bind(_=self.on_lang)
        super(MySpecialLabel, self).__init__(**kwargs)

    def on_lang(self, instance, value):
            self.text = self.app._('Running')

class LangApp(App):
    lang = StringProperty('en')
    _ = ObjectProperty(None, allownone=True)

    def build(self):
        self.switch_lang(self.lang)

    def on_lang(self, instance, lang):
        self.switch_lang(lang)

    def switch_lang(self, lang):
        locale_dir = join(dirname(__file__), 'data', 'locales')
        locales = gettext.translation('langapp', locale_dir, languages=[self.lang])
        self._ = locales.ugettext


LangApp().run()
