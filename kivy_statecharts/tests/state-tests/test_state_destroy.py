'''
Statechart tests, state destroy
===============================
'''

import unittest, re

counter = 0

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy_statecharts.system.state import State
from kivy_statecharts.system.empty_state import EmptyState
from kivy_statecharts.system.empty_state import EMPTY_STATE_NAME
from kivy_statecharts.system.statechart import StatechartManager

import os, inspect

class Statechart_1(StatechartManager):
    def __init__(self, **kwargs):
        kwargs['root_state_class'] = self.RootState
        kwargs['trace'] = True
        super(Statechart_1, self).__init__(**kwargs)

    class RootState(State):
        def __init__(self, **kwargs):
            kwargs['initial_substate_key'] = 'A'
            super(Statechart_1.RootState, self).__init__(**kwargs)

        class A(State):
            def __init__(self, **kwargs):
                super(Statechart_1.RootState.A, self).__init__(**kwargs)

        class B(State):
            def __init__(self, **kwargs):
                kwargs['substates_are_concurrent'] = True
                super(Statechart_1.RootState.B, self).__init__(**kwargs)

            class X(State):
                def __init__(self, **kwargs):
                    super(Statechart_1.RootState.B.X, self).__init__(**kwargs)

            class Y(State):
                def __init__(self, **kwargs):
                    super(Statechart_1.RootState.B.Y, self).__init__(**kwargs)

class StateAddSubstateTestCase(unittest.TestCase):
    def setUp(self):
        global statechart_1
        global root_state_1
        global monitor_1
        global state_A
        global state_B
        global state_X
        global state_Y

        statechart_1 = Statechart_1()
        statechart_1.init_statechart()
        root_state_1 = statechart_1.root_state_instance
        monitor_1 = statechart_1.monitor
        state_A = statechart_1.get_state('A')
        state_B = statechart_1.get_state('B')
        state_X = statechart_1.get_state('X')
        state_Y = statechart_1.get_state('Y')
        
    # Destroy a state
    def test_destroy(self):
        self.assertIsNotNone(state_B)
        self.assertEqual(len(state_B.substates), 2)

        state_B.destroy()

        self.assertEqual(len(state_B.substates), 0)
        self.assertEqual(len(state_B.current_substates), 0)
        self.assertEqual(len(state_B.entered_substates), 0)
        self.assertIsNone(state_B.parent_state)
        self.assertIsNone(state_B.history_state)
        self.assertIsNone(state_B.initial_substate_key)
        self.assertIsNone(state_B.initial_substate_object)
        self.assertIsNone(state_B.statechart)
        self.assertIsNone(state_B.owner)
