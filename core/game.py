import state

class Game():
    def __init__(self, g, states, state_name):
        self.g = g
        self.states = states
        self.cur_state = self.states[state_name]

    def run(self):
        isRunning = True
        while isRunning:
            choice = self.g.show_menu( self.cur_state.menu )
            self.cur_state.update( choice )
            if self.cur_state.done == True:
                if self.cur_state.next_state == None:
                    isRunning = False
                else:
                    self.next_state( self.cur_state.next_state )

    def next_state(self, state_name):
        self.cur_state = self.states[ state_name ]
