from transitions.extensions import GraphMachine

from utils import send_text_message 

from warriors import func ,funcin

from transitions.extensions import GraphMachine 

#pygraphviz = "==1.5"

playerindex=8

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_state2(self, event):
        text = event.message.text
        return  "player" in text.lower()

    def is_going_to_state3(self, event):
        text = event.message.text
        return "data" in text.lower()

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        URL="https://www.basketball-reference.com/teams/GSW/2022.html"
        a=func(URL,0,0,0)
        send_text_message(reply_token,a)
        #self.go_back()

    #def on_exit_state1(self):
     #   print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        text = event.message.text
        global playerindex
        playerindex=text.split()[1]
        URL="https://www.basketball-reference.com/teams/GSW/2022.html"
        a=func(URL,1,playerindex,0)
        reply_token = event.reply_token
        send_text_message(reply_token,a)
        #self.go_back()

    def on_enter_state3(self, event):
        global playerindex
        print("I'm entering state3")
        text = event.message.text
        dataindex=text.split()[1]
        URL="https://www.basketball-reference.com/teams/GSW/2022.html"
        a=func(URL,2,playerindex,dataindex)
        reply_token = event.reply_token
        send_text_message(reply_token,a)
        self.go_back()
