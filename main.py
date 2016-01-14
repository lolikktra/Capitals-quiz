#!usr\bin\kivy
# -*- coding: utf-8 -*-
__version__ = "1.0"

import kivy

kivy.require('1.7.2')

from sys import exit
from random import sample, choice 

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

en_states_l1 = {"Austria": "Vienna", "Great Britain": "London",
                 "Germany": "Berlin", "Ireland": "Dublin",
                 "Luxembourg": "Luxembourg", "Monaco": "Monaco",
                 "Netherlands": "Amsterdam", "France": "Paris",
                 "Bulgaria": "Sofia", "Hungary": "Budapest",
                 "Poland": "Warsaw", "Romania": "Bucharest",
                 "Czech Republic": "Prague", "Denmark": "Copenhagen",
                 "Norway": "Oslo", "Finland": "Helsinki",
                 "Sweden": "Stockholm", "Greece": "Athens",
                 "Spain": "Madrid", "Italy": "Rome",
                 "Russia": "Moscow", "Argentina": "Buenos Aires",
                 "Brazil": "Brasilia", "India": "New Deli",
                 "China": "Beijing", "Japan": "Tokyo",
                 "Egypt": "Cairo", "Sao Tome and Principe": "Sao Tome",
                 "Senegal": "Dakar", "Tunisia": "Tunis",
                 "Canada": "Ottawa", "Mexico": "Mexico City",
                 "USA": "Washington", "Guatemala": "Guatemala City",
                 "Panama": "Panama City", "Cuba": "Havana",
                 "Uruguay": "Montevideo", "Chile": "Santiago",
                 "Australia": "Canberra"}

states_level2 = {"Andorra": "Andorra la Vella", "Belgium": "Brussels",
                 "Switzerland": "Bern", "Slovakia": "Bratislava",
                 "Iceland": "Reykjavik", "Portugal": "Lisbon",
                 "San Marino": "San Marino", "Croatia": "Zagreb",
                 "Turkey": "Ankara", "Afghanistan": "Kabul",
                 "Algeria": "Algiers", "Djibouti": "Djibouti",
                 "Israel": "Jerusalem", "Indonesia": "Jakarta",
                 "Iraq": "Baghdad", "Iran": "Tehran",
                 "Kuwait": "Kuwait", "Mongolia": "UlaanBaatar",
                 "Nepal": "Kathmandu", "United Arab Emirates": "Abu Dhabi",
                 "Pakistan": "Islamabad", "Saudi Arabia": "Riyadh",
                 "Singapore": "Singapore", "Syria": "Damascus",
                 "Thailand": "Bangkok", "Philippines": "Manila",
                 "Guinea-Bissau": "Bissau", "Madagascar": "Antananarivo",
                 "South Africa": "Pretoria", "El Salvador": "San Salvador",
                 "Venezuela": "Caracas", "Colombia": "Bogota",
                 "Paraguay": "Asuncion", "Peru": "Lima",
                 "Ecuador": "Quito", "New Zealand": "Wellington",
                 "Malaysia": "Kuala Lumpur", "South Korea": "Seoul",
                 "Libya": "Tripoli"}

states_level3 = {"Belarus": "Minsk", "Moldova": "Chisinau",
                 "Ukraine": "Kiev", "Latvia": "Riga",
                 "Lithuania": "Vilnius", "Estonia": "Tallinn",
                 "Albania": "Tirana", "Bosnia and Herzegovina": "Sarajevo",
                 "Macedonia": "Skopje", "Serbia": "Belgrade",
                 "Slovenia": "Ljubljana", "Montenegro": "Podgorica",
                 "Azerbaijan": "Baku", "Georgia": "Tbilisi",
                 "Kazakhstan": "Astana", "Armenia": "Yerevan",
                 "Vietnam": "Hanoi", "Cyprus": "Nicosia",
                 "Papua New Guinea": "Port Moresby", "Tajikistan": "Dushanbe",
                 "Turkmenistan": "Ashgabat", "Uzbekistan": "Tashkent",
                 "Congo": "Kinshasa", "Angola": "Luanda",
                 "Ethiopia": "Addis Ababa", "Kenya": "Nairobi",
                 "Bangladesh": "Dhaka", "Morocco": "Rabat",
                 "Somalia": "Mogadishu", "Honduras": "Tegucigalpa",
                 "Haiti": "Port-au-Prince", "Jamaica": "Kingston",
                 "Guyana": "Georgetown", "Suriname": "Paramaribo",
                 "Qatar": "Doha", "Kyrgyzstan": "Bishkek",
                 "North Korea": "Pyongyang", "Bolivia": "Sucre",
                 "Nigeria": "Abuja"}

states_level4 = {"Bahamas": "Nassau", "Bahrain": "Manama", 
                 "Maldives": "Male", "Benin": "Porto-Novo",
                 "Bhutan": "Thimphu", "Laos": "Vientiane",
                 "Botswana": "Gaborone", "Burkina Faso": "Ouagadougou",
                 "Burundi": "Bujumbura", "Cambodia": "Phnom Penh",
                 "Yemen": "Sana'a", "Belize": "Belmopan",
                 "Liechtenstein": "Vaduz", "Malta": "Valletta",
                 "Lebanon": "Beirut", "Oman": "Muscat",
                 "Gambia": "Banjul", "Ghana": "Accra",
                 "Guinea": "Conakry", "Equatorial Guinea": "Malabo",
                 "Cameroon": "Yaounde", "Congo Republic": "Brazzaville",
                 "Ivory Coast": "Yamoussoukro", "Liberia": "Monrovia",
                 "Malawi": "Lilongwe", "Mozambique": "Maputo",
                 "Sudan": "Khartoum", "Seychelles": "Victoria",
                 "Uganda": "Kampala", "Central African Republic": "Bangui",
                 "Chad": "N'Djamena", "Costa Rica": "San Jose",
                 "Nicaragua": "Managua", "Sri Lanka": "Colombo",
                 "Palau": "Ngerulmud", "Gabon": "Libreville",
                 "Fiji": "Suwa", "Jordan": "Amman"}

states_level5 = {"Kiribati": "Tarawa", "Marshall Islands": "Majuro",
                 "Antigua and Barbuda": "Saint John's", "Tonga": "Nuku'alofa",
                 "Saint Vincent and the Grenadines": "Kingstown", "Tuvalu": "Funafuti",
                 "Brunei": "Bandar Seri Begawan", "Cabo Verde": "Praia",
                 "Solomon Islands": "Honiara", "Samoa": "Apia",
                 "Myanmar": "Naypyidaw", "East Timor": "Dili",
                 "Nauru": "Yaren", "Federated States of Micronesia": "Palikir",
                 "Eritrea": "Asmara", "Zambia": "Lusaka",
                 "Zimbabwe": "Harare", "Comoros": "Moroni",
                 "Lesotho": "Maseru", "Mauritius": "Port Louis",
                 "Mauritania": "Nouakchott", "Mali": "Bamako",
                 "Niger": "Niamey", "Rwanda": "Kigali",
                 "Swaziland": "Lobamba", "Namibia": "Windhoek",
                 "Sierra Leone": "Freetown", "Tanzania": "Dodoma",
                 "Togo": "Lome", "Grenada": "St. George's",
                 "Dominica": "Roseau", "Dominican Republic": "Santo Domingo",
                 "Saint Kitts and Nevis": "Basseterre", "Saint Lucia": "Castries",
                 "Trindad and Tobago": "Port of Spain", "Vanuatu": "Port Vila",
                 "Barbados": "Bridgetown", "South Sudan": "Juba"}


class MenuWindow(Screen):

    def __init__(self, **kwargs):
        super(MenuWindow, self).__init__(**kwargs)
        menubox = BoxLayout(orientation='vertical', padding=50, spacing=50)
        playbtn = Button(text='Play', font_size='20sp', italic=True)
        playbtn.bind(on_press=self.game)
        menubox.add_widget(playbtn)
        languagebtn = Button(text='Language', font_size='20sp', italic=True)
        languagebtn.bind(on_press=self.language)
        menubox.add_widget(languagebtn)
        aboutbtn = Button(text='About', font_size='20sp', italic=True)
        aboutbtn.bind(on_press=self.about)
        menubox.add_widget(aboutbtn)
        quitbtn = Button(text='Quit', font_size='20sp', italic=True)
        quitbtn.bind(on_press=self.quit)
        menubox.add_widget(quitbtn)
        self.add_widget(menubox)

    def game(self, button):
        self.manager.current = 'play'

    def language(self, button):
        self.manager.current = 'language'

    def about(self, button):
        self.manager.current = 'about'

    def quit(self, button):
        exit(0)

class AboutGame(Screen):

    def __init__(self, **kwargs):
        super(AboutGame, self).__init__(**kwargs)
        aboutgamebox = BoxLayout(orientation='vertical', padding=10, spacing=10)
        aboutlbl = Label(text="This is 'Capitals' quiz")
        aboutgamebox.add_widget(aboutlbl)
        backbtn = Button(text='Back to Menu')
        backbtn.bind(on_press=self.back_to_menu)
        aboutgamebox.add_widget(backbtn)
        self.add_widget(aboutgamebox)		

    def back_to_menu(self, button):
        self.manager.current = 'menu'


class ChangeLanguage(Screen):

    def __init__(self, **kwargs):
        super(ChangeLanguage, self).__init__(**kwargs)
        langbox = BoxLayout(orientation='vertical', padding=50, spacing=50)
        enbtn = Button(text='English', font_size='20sp', italic=True)
        enbtn.bind(on_press=self.en_language)
        langbox.add_widget(enbtn)
        ukrbtn = Button(text='Ukrainian', font_size='20sp', italic=True)
        ukrbtn.bind(on_press=self.ukr_language)
        langbox.add_widget(ukrbtn)
        self.add_widget(langbox)

    def en_language(self, button):
        # need to add later checking if language is English
        self.manager.current = 'menu'

    def ukr_language(self, button):
        # need to add later transforming language to Ukrainian
        self.manager.current = 'menu'


class PlayGame(Screen):

    def __init__(self, **kwargs):
        super(PlayGame, self).__init__(**kwargs)

    def on_enter(self):
        self.add_widget(QuizWindow())


class TimeLabel(Label):
    def __init__(self, **kwargs):
        super(TimeLabel, self).__init__(size_hint=(1, .2))
        self.time = 15

    def update(self, *args):
        self.time -= 1
        self.text = "You have %d seconds to answer" %(self.time)


class QuizWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(QuizWindow, self).__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.score = 0
        self.level = 1
        self.questions = []
        self.round()

    def ansresult(self, instance):
        # invokes by pressing button Answer
        
        # stops all clock shedules
        Clock.unschedule(self.time_label.update)
        Clock.unschedule(self.timeend)

        # checks whether user gave right answer
        # and invokes window with answering result
        for i in self.togglebuttonlist:
            if i.text == self.states[self.guess_state]:
                i.background_color = (0, 1, 0, 1)
                if i.state == "down":
                    self.score += 1
                    if self.score % 10 == 0:
                        self.level += 1
                        if self.level == 6:
                            text = "You win!"
                            btnaction = self.gameover
                    text = "Congratulations! Your score is %d" %(self.score)
                    
                    btnaction = self.nextround
                else:
                    text = "You are lost!"
                    btnaction = self.gameover

        content = Button(text=text)				
        self.answerresult = Popup(title="", content=content, size_hint=(.8, .5))
        content.bind(on_press=btnaction)
        self.answerresult.open()

    def nextround(self, instance):
        self.clear_widgets()
        self.answerresult.dismiss()
        self.round()

    def gameover(self, instance):
        # invokes new window with ability
        # to start new game or exit
        self.answerresult.dismiss()
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="You are lost!", size_hint=(.8, 1)))
        box.add_widget(Label(text="Do you want to start new game?"))
        selectbuttons = BoxLayout(spacing=10)
        yesbutton = Button(text="Yes")
        yesbutton.bind(on_press=self.newgame)
        selectbuttons.add_widget(yesbutton)
        nobutton = Button(text="No")
        nobutton.bind(on_press=self.exitgame)
        selectbuttons.add_widget(nobutton)
        box.add_widget(selectbuttons)
        self.gameoverpopup = Popup(title="", content=box, size_hint=(.8, .5))
        self.gameoverpopup.open()

    def newgame (self, instance):
        self.score = 0
        self.level = 1
        self.questions = []
        self.clear_widgets()
        self.gameoverpopup.dismiss()
        self.round()

    def exitgame(self, instance):
        exit(0)
		
    def round(self):
        # first game round, appears when game starts
        
        if self.level == 1:
            self.states = states_level1
        elif self.level == 2:
            self.states = states_level2
        elif self.level == 3:
            self.states = states_level3
        elif self.level == 4:
            self.states = states_level4
        elif self.level == 5:
            self.states = states_level5

        self.guess_list = sample(self.states, 5)
        self.guess_state = choice(self.guess_list)

        if self.guess_state in self.questions:
            self.guess_state = choice(self.guess_list)
            self.questions.append(self.guess_state)
        else:
            self.questions.append(self.guess_state)

        # player's score and level widget
        scorelayout = BoxLayout(padding=10, size_hint=(1, .2))
        self.scorelabel = Label(text="Score: %d" %(self.score))
        self.levellabel = Label(text="Level: %d" %(self.level))
        scorelayout.add_widget(self.scorelabel)
        scorelayout.add_widget(self.levellabel)
        self.add_widget(scorelayout)

        # question widget
        self.question = Label(text="What is the capital of %s?" %(self.guess_state), 
                              size_hint=(1, .3))
        self.add_widget(self.question)

        # variants of answer widget
        self.togglebuttonlist = []		
        for i in self.guess_list:
            self.btn = ToggleButton(text=self.states[i], group='cap', size_hint=(1, .1))
            self.add_widget(self.btn)
            self.togglebuttonlist.append(self.btn)

        # label with remaining time for the answer
        self.time_label = TimeLabel()
        Clock.schedule_interval(self.time_label.update, 1)		
        self.add_widget(self.time_label)

        # button, that submits user's answer
        answerbtn = Button(text="Answer",size_hint=(.45, .1))
        answerbtn.bind(on_press=self.ansresult)
        self.add_widget(answerbtn)

        Clock.schedule_once(self.timeend, self.time_label.time)

    def timeend(self, dt):
        self.ansresult(1)


class MyApp(App):

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def build(self):
        self.icon = "icon.png"
        start = ScreenManager()
        screen1 = MenuWindow(name='menu')
        screen2 = ChangeLanguage(name='language')
        screen3 = AboutGame(name='about')
        screen4 = PlayGame(name='play')
        start.add_widget(screen1)
        start.add_widget(screen2)
        start.add_widget(screen3)
        start.add_widget(screen4)
        return start

if __name__ == '__main__':
    MyApp().run()
