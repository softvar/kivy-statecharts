'''
Statechart tests, owner
===========
'''

import unittest

counter = 0

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy_statechart.system.state import State
from kivy_statechart.system.statechart import StatechartManager

import os, inspect

class Owner_1_MC(type):
    def __repr__(self):
        return 'Owner_1'
class Owner_1(object):
    __metaclass__ = Owner_1_MC

class Owner_2_MC(type):
    def __repr__(self):
        return 'Owner_2'
class Owner_2(object):
    __metaclass__ = Owner_2_MC

class Owner_3_MC(type):
    def __repr__(self):
        return 'Owner_3'
class Owner_3(object):
    __metaclass__ = Owner_3_MC

class TestState(State):
    accessedOwner = ObjectProperty(None)
      
    def reset(self):
        setattr(self, 'accessedOwner', None)
      
    def render(self):
        setattr(self, 'accessedOwner', self.owner)
      
class TestStatechart(StatechartManager):
    def render(self):
        self.invokeStateMethod('render')

class A(TestState):
    def foo(self):
        self.gotoState('B')

class B(TestState):
    def bar(self):
        self.gotoState('A')

class Z(TestState):
    pass 

class Y(TestState):
    initialSubstate = 'Z'

    Z = Z

class X(TestState):
    initialSubstate = 'Y'

    Y = Y

class Statechart_1(TestStatechart):
    initialState = 'A'
      
    A = A
    B = B
    X = X

class C(TestState):
    def foo(self):
        self.gotoState('D')

class D(TestState):
    def bar(self):
        self.gotoState('C')

class Statechart_2(TestStatechart):
    owner = Owner_2
    initialState = 'C'
      
    C = C
    D = D

class E(TestState):
    def foo(self):
        self.gotoState('F')

class F(TestState):
    def bar(self):
        self.gotoState('E')

class Statechart_3(TestStatechart):
    statechartOwnerKey ='fooOwner'
    fooOwner = Owner_3
    initialState = 'E'
      
    E = E
    F = F

class StatechartOwnerTestCase(unittest.TestCase):
    def setUp(self):
        global statechart_1
        global statechart_2
        global statechart_3
        global owner_1
        global owner_2
        global owner_3
        global rootState_1
        global rootState_2
        global rootState_3
        global state_A
        global state_B
        global state_C
        global state_D
        global state_E
        global state_F
        global state_X
        global state_Y
        global state_Z

        statechart_1 = Statechart_1()
        rootState_1 = statechart_1.rootState
        owner_1 = Owner_1()
        state_A = statechart_1.getState('A')
        state_B = statechart_1.getState('B')
        state_X = statechart_1.getState('X')
        state_Y = statechart_1.getState('Y')
        state_X = statechart_1.getState('X')
        state_Z = statechart_1.getState('Z')
        
        statechart_2 = Statechart_2()
        rootState_2 = statechart_2.rootState
        owner_2 = Owner_1()
        state_C = statechart_2.getState('C')
        state_D = statechart_2.getState('D')

        statechart_3 = Statechart_3()
        rootState_3 = statechart_3.rootState
        owner_3 = Owner_1()
        state_E = statechart_3.getState('E')
        state_F = statechart_3.getState('F')

    # Basic owner get and set
    def test_statechart_1(self):
        self.assertEqual(rootState_1.owner, statechart_1) 
        self.assertEqual(state_A.owner, statechart_1) 
        self.assertEqual(state_B.owner, statechart_1) 
        self.assertEqual(state_X.owner, statechart_1) 
        self.assertEqual(state_Y.owner, statechart_1) 
        self.assertEqual(state_Z.owner, statechart_1) 

        statechart_1.owner = owner_1

        self.assertEqual(rootState_1.owner, owner_1) 
        self.assertEqual(state_A.owner, owner_1) 
        self.assertEqual(state_B.owner, owner_1) 
        self.assertEqual(state_X.owner, owner_1) 
        self.assertEqual(state_Y.owner, owner_1) 
        self.assertEqual(state_Z.owner, owner_1) 

