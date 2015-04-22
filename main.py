from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.app import App

from os.path import join, dirname
import gettext


class I18NLabel(Label):
    source_text = StringProperty('')

class MySpecialLabel(I18NLabel):
    def __init__(self, **kwargs):
        super(MySpecialLabel, self).__init__(**kwargs)
        self.source_text = 'Running'

class LangApp(App):
    lang = StringProperty('en')
    _ = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        self.switch_lang(self.lang)
        super(LangApp, self).__init__(**kwargs)

    def on_lang(self, instance, lang):
        self.switch_lang(lang)

    def switch_lang(self, lang):
        locale_dir = join(dirname(__file__), 'data', 'locales')
        locales = gettext.translation('langapp', locale_dir, languages=[self.lang])
        self._ = locales.ugettext


LangApp().run()
