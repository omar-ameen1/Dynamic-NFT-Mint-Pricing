from abc import ABC, abstractmethod
from mimetypes import init
from operator import mod
import numpy as np


class AlgoClass:
    def __init__(self, goal_sales_per_block, initial_price, update_freq, profit=0):
        self.goal_sales_per_block = goal_sales_per_block
        self.price = initial_price
        self.block_arr = []
        self.profit = profit
        self.update_freq = update_freq
        self.initial_price = initial_price
        self.current_ema = 0
        self.profit = 0
        self.ema_array = []
        self.current_dema = 0
        
    def get_price(self):
        return self.price

    def calc_wts(self, most_recent_sales):
        if (len(self.block_arr) <= self.update_freq):
            ema = 0
            dema = 0
        else:
            ema = 0.2 * most_recent_sales + self.current_ema * (1 - 0.2)
            dema = 2 * ema - (0.2 * self.ema_array[-1] + self.current_dema * (1 - 0.2))
        self.current_ema = ema
        self.current_dema = dema
        self.ema_array.append(ema)
        self.profit += self.price * most_recent_sales
        self.self_monitor()
        return dema
    
    def calc_wts_no_call(self):
        return self.current_ema

    def check_rate(self):
        ratio = self.calc_wts_no_call()/self.goal_sales_per_block
        return ratio

    def change_price(self):
        ratio = self.check_rate()
        if (ratio > 1):
            self.price = self.price * \
                (self.calc_wts_no_call() / self.goal_sales_per_block)
        elif (ratio < 1):
            self.price = self.price * 0.95
        else:
            pass

    def self_monitor(self):
        if (len(self.block_arr) % self.update_freq == 0):
            self.change_price()
        else:
            pass
    
    def get_profit(self):
        return self.profit

    def reset(self):
        self.__init__


class block:
    def __init__(self, index, sales=0):
        self.sales = sales
        self.index = index

    def get_sales(self):
        return self.sales

    def add_sales(self):
        self.sales += 1

    def set_sales(self, num):
        self.sales = num

