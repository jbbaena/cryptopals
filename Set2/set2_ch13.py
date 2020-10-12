#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 12:45:51 2019

@author: Javier Verbel
Cryptopals Set 2 Challenge 13
"""
import random
initial = "foo=bar&baz=qux&zap=zazzle"

def par(entrada):
    a = entrada.split("&")
    return {"foo":a[0].split("foo=")[1], "baz":a[1].split("baz=")[1], "zap":a[2].split("zap=")[1]}


print(initial.find("&"))
print(initial.strip("="))
print(initial.__contains__("&"))
print(initial.__contains__("="))

def profile_for(email):
    if initial.__contains__("=") or initial.__contains__("&"):
        print("Invalid email")
    else:
        a = email.split("@")
        return "email="+ a[0] + str()