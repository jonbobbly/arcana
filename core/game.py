class Game():
    def __init__(self, states, state_name, persist):
        self.persist = persist
        self.states = states
        self.cur_state = self.states[state_name]
        self.cur_state.enter()

    def run(self):
        isRunning = True
        while isRunning:
            self.cur_state.run()
            if self.cur_state.done == True:
                if self.cur_state.next_state == None:
                    isRunning = False
                else:
                    self.next_state( self.cur_state.next_state )

    def next_state(self, state_name):
        self.persist["g"].clearscreen()
        self.cur_state.exit()
        self.cur_state = self.states[ state_name ]
        self.cur_state.enter()
