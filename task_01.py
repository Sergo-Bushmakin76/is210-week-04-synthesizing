#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temperature conversion program"""


from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')


def celsius_to_kelvin(degrees):
    """Accepts celsius and computes it into kelvin.
    Args:
        degrees (int): Arg representing degrees celsius.
    Returns:
        decimal: Computes degrees variable and returns as decimal.
    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')
    """
    return Decimal(ABSOLUTE_DIFFERENCE+degrees)


def fahrenheit_to_celsius(degrees):
    """Accepts fahrenheit and computes it into degrees celsius.
    Args:
        degrees (int): Arg representing degrees celsius.
    Returns:
        decimal: Computes degrees variable and returns as decimal.
    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        >>> fahrenheit_to_celsius(26.389)
        Decimal('-3.1172222222222227827614915440790355205535888671875')
    """
    return Decimal(((int(degrees)-32)*5.0)/9)


def fahrenheit_to_kelvin(degrees):
    """Accepts fahrenheit and computes it into kelvin.

    Args:
        degrees (int): Arg representing degrees celsius.

    Returns:
        decimal: Computes degrees in variable and returns as decimal.
    Examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('375.15')
    """
    return Decimal(celsius_to_kelvin(fahrenheit_to_celsius(degrees)))
