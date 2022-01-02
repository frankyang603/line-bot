from transitions.extensions import GraphMachine

from utils import send_text_message 

from warriors import func ,funcin

from transitions.extensions import GraphMachine 

#pygraphviz = "==1.5"
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("FSM.png", prog= 'dot') #new add

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    # def is_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state2"

    def is_going_to_state2(self, event):
        text = event.message.text
        return  "player" in text.lower()

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        URL="https://www.basketball-reference.com/teams/GSW/2022.html"
        a=func(URL,0)
        send_text_message(reply_token,a)
        #send_text_message(reply_token, "Trigger state1")
        #self.go_back()

    #def on_exit_state1(self):
     #   print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()

    #def on_exit_state2(self):
     #   print("Leaving state2")
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    #def on_exit_state3(self):
     #   print("Leaving state3")
