# -*- coding: utf-8 -*-

settings = {
    'source': 'csv',
    #'source': 'mongodb',
    'data_path': './data',
    'stock_commission': 3 / 10000.0,
    'future_commission': 1 / 10000.0,
    'tick_test': False,
}


class ConfigLog(object):
    log_level = 'INFO'
    log_to_file = True
    log_to_console = True
    log_path = './log'

class ConfigColor:
    bar_up_color = 'gray'
    bar_down_color = 'k'
    bar_width = 1
    bar_line_color = 'k'
    bar_alpha = 0.5
    vol_up_color = 'gray'
    vol_down_color = 'k'
    vol_width = 1
    vol_alpha = 0.5
    trading_up_color = 'pink'
    trading_down_color = 'skyblue'
    trading_width = 2
    trading_alpha = 0.7
    plot_line_alpha = 1

__all__ = ['settings', 'ConfigLog', 'ConfigColor']
