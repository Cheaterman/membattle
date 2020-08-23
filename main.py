from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger

from MBlogicVrsta import pictures_matrix4

try:
    import mysql.connector
    from mysql.connector import Error

except ImportError:
    Logger.warning('Database: MySQL module not found.')

else:
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='membattle',
                                             user='root',
                                             password='')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)


Window.clearcolor = (1, 0.3, 0, 1)


class MyGridLog(Widget):
    def CompBtn(self):
        Pop6.show_popup(self)


class MyGrid(Widget):
    def CompBtn(self):
        Pop5.show_popup(self)


class MyGridS(Widget):  # sign up
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""

    def DBsend(self, Pass, User):
        if Pass == "" or User == "":
            Pop5.show_popup(self)
            return
        try:
            prva = (
                "INSERT INTO `user` "
                "(`Username`, `Password`, `Mail`, `Age`, `UserID`) "
                "VALUES (%s, %s, 'dada', '31', '');"
            )
            druga = (Pass.text, User.text)
            cursor.execute(prva, druga)
            connection.commit()

        except Error:
            Pop1.show_popup1(self)
            # print('this username is already taken')


class MyGridT(Widget):  # Log in
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""

    def DBrecieve(self, User, Pass):
        global userL

        cursor.execute("SELECT Username,Password FROM user")
        mycursor = cursor.fetchall()
        userL = []
        passL = []
        for i in mycursor:
            userL.append(i[0])
            passL.append(i[1])
        print(userL, passL)

        if User.text not in userL:
            Pop2.show_popup2(self)
        else:
            global userIndex
            ind = userL.index(User.text)
            userIndex = ind
            if Pass.text == passL[ind]:
                Pop4.switch(self)
                Pop4.show_popup(self)
            else:
                Pop3.show_popup(self)


class AboutWindowLog(Screen):
    pass


class ForgotPass(Widget):
    def clear_inputs(self, text_inputs):
        for text_input in text_inputs:
            text_input.text = ""

    def btn(self):
        Pop.show_popup(self)
        inst = IncrediblyCrudeClock()
        inst.start()
        self.ids.jam.add_widget(inst)

    def callback(self, *args):
        self.ids.send.disabled = True


class ForgotPassSc(Screen):
    pass


class WindowMan(ScreenManager):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class AboutWindow(Screen):
    pass


class TransitionWindow(Screen):
    pass


class SelectionWindow(Screen):
    pass


class PracticeWindow(Screen):
    pass


class CompWindow(Screen):
    pass


class MainWindow(Screen):
    pass


class MainLogWindow(Screen):
    def on_enter(self):
        print(userL[userIndex])
        self.ids.logpuzz.ids.logedin.text = (
            f'Logged in as: {userL[userIndex]}'
        )


class StarScWindow(Screen):
    def on_enter(self, *args):
        self.count = 3
        self.countdown_label = Label(
            font_size=150,
            bold=True,
            color=(0.2, 0.9, 0.9, 1),
        )
        self.countdown_label.text = str(self.count)
        Clock.schedule_once(self.update_count, 1)
        self.ids.hello.add_widget(self.countdown_label)
        Clock.schedule_once(self.switch, 3)

    def update_count(self, *args):
        self.count -= 1
        if self.count > -1:
            self.countdown_label.text = str(self.count)
            Clock.schedule_once(self.update_count, 1)

    def switch(self, *args):
        self.parent.current = 'puzzle'
        self.ids.hello.remove_widget(self.countdown_label)


class StarScWindowC(Screen):
    def on_enter(self, *args):
        self.count = 3
        self.countdown_label = Label(
            font_size=150,
            bold=True,
            color=(0.2, 0.9, 0.9, 1),
        )
        self.countdown_label.text = str(self.count)
        Clock.schedule_once(self.update_count, 1)
        self.ids.helloC.add_widget(self.countdown_label)
        Clock.schedule_once(self.switchC, 3)

    def update_count(self, *args):
        self.count -= 1
        if self.count > -1:
            self.countdown_label.text = str(self.count)
            Clock.schedule_once(self.update_count, 1)

    def switchC(self, *args):
        self.parent.current = 'puzzleComp'
        self.ids.helloC.remove_widget(self.countdown_label)


class Pop(FloatLayout):
    def show_popup(self):
        show = Pop()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(200, 100),
        )
        popupWindow.open()


class Pop1(FloatLayout):
    def show_popup1(self):
        show = Pop1()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(250, 100),
        )
        popupWindow.open()


class Pop2(FloatLayout):
    def show_popup2(self):
        show = Pop2()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(200, 100),
        )
        popupWindow.open()


class Pop3(FloatLayout):
    def show_popup(self):
        show = Pop3()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(250, 110),
        )
        popupWindow.open()


class Pop4(FloatLayout):
    def show_popup(self):
        show = Pop4()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(200, 110),
        )
        popupWindow.open()

    def switch(self, *args):
        self.parent.parent.current = 'mainlogin'
        self.parent.parent.transition.direction = 'right'


class Pop5(FloatLayout):
    def show_popup(self):
        show = Pop5()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(200, 115),
        )
        popupWindow.open()


class Pop6(FloatLayout):
    def show_popup(self):
        show = Pop6()
        popupWindow = Popup(
            title="Note",
            content=show,
            size_hint=(None, None),
            size=(200, 115),
        )
        popupWindow.open()


class IncrediblyCrudeClock(Label):
    a = NumericProperty(30)

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)

        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = ""

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)


class PuzzleWindow(Screen):
    def on_enter(self):
        ran_list4str = pictures_matrix4()[0]
        ran_list4 = pictures_matrix4()[1]

        for i in range(len(self.ids.puzz.ids.puzzG.children[:])):
            self.ids.puzz.ids.puzzG.children[i].trigger_action(2)
            self.ids.puzz.ids.puzzG.children[i].a = ran_list4[i]
            self.ids.puzz.ids.puzzG.children[i].text = ran_list4str[i]
            self.ids.puzz.ids.puzzG.children[i].color = (1, 0, 0, 0)
            self.ids.puzz.ids.puzzG.children[i].bind(
                on_press=lambda x: self.newspress()
            )

    def on_leave(self):
        for i in range(len(self.ids.puzz.ids.puzzG.children[:])):
            self.ids.puzz.ids.puzzG.children[i].trigger_action()

        self.ids.puzz.ids.resign.children[0].trigger_action()
        self.ids.puzz.ids.finish.children[0].trigger_action()

    def newspress(self, *args):
        self.a = "C:/Users/Maj/Desktop/images1.jpg"
        self.back_color = (1, 0, 1, 1)
        print('got you')


class PuzzleWindowComp(Screen):
    pass


class MemBattleV1(App):
    pass


if __name__ == '__main__':
    app = MemBattleV1()
    app.run()
