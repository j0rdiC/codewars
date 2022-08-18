# 6 kyu
# https://www.codewars.com/kata/5268acac0d3f019add000203/train/python


class Automaton(object):


    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        self.states = ['q1']
        for n in commands:
            if n == '1':
                if self.states[-1] == 'q1':
                    self.states.append('q2')
                elif self.states[-1] == 'q2':
                    self.states.append('q1')
                elif self.states[-1] == 'q3':
                    self.states.append('q2')
                
            elif n == '0':
                if self.states[-1] == 'q1':
                    self.states.append('q1')
                elif self.states[-1] == 'q2':
                    self.states.append('q2')
                elif self.states[-1] == 'q3':
                    self.states.append('q3')
        return self.states[-1] == 'q2'

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.

my_automaton.read_commands(["1"])#, True)
my_automaton.read_commands(["1", "0", "0", "1"])#, True)