"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random

class NinjaGold(Controller):
    def __init__(self, action):
        super(NinjaGold, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        session['gold'] = 0
        session['count'] = 0
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view("index.html", gold = session['gold'])

    def process_money(self):
        session['count'] += 1
        if request.form['building'] == 'farm':
            print 'farm'
            session['gold'] = session['gold'] + (round(random.random()*10))+10
            msg = "\n You walk into the dank farm, reeking of hey and animal dung. \n You found "+str(session['gold'])+" gold!...in a cow pie...ew... \n "
        elif request.form['building'] == 'cave':
            print 'cave'
            session['gold'] = session['gold'] + random.randint(5,10)
            msg = "\n You walk into the cold and damp cave as quietly as you can. \n You found "+str(session['gold'])+" gold!...in the carcus of a fresh bear meal...ew... \n "
        elif request.form['building'] == 'house':
            print 'house'
            session['gold'] = session['gold'] + random.randint(2,5)
            msg = "\n You walk into a warm home, hopefully its yours! \n You stole "+str(session['gold'])+" gold!...in your neighbor's purse...thats low man... \n "
        elif request.form['building'] == 'casino':
            print 'casino'
            session['gold'] = session['gold'] + random.randint(0,100)-50
            if session['gold'] < 0:
                msg = "\n You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck. \n You lost "+str(session['gold'] * -1)+" gold!...\n Bazooko's Circus is what the world would be doing every Saturday night if the Nazis had won the war. This was the Sixth Reich.\n"
            elif session['gold'] > 0:
                msg = "\n You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck. \n You won "+str(session['gold'])+" gold!... \n ...that vision of the big winner somehow emerging from the last minute pre-dawn chaos of a stale Vegas casino.\n"
            elif session['gold'] == 0:
                msg = "\n You walk into a smelly casino called Bazooko's Circus, you plunk down next to a car salesmen and try your luck. \n You broke even!... \n ...Too weird to live, and too rare to die... \n "
        session['message'] += msg
        return self.load_view("index.html", gold = session['gold'], info = session['message'])

