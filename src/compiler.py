#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from os import system
# define fuctions and root variables
repeatI = 1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def compressListName(name) :
  tempStr = ""
  if(name[-1] == ']') :
    for letter in list(name) :
      if(letter == "[") :
        break
      tempStr = (tempStr + letter)
  else :
      tempStr = name
  return(tempStr)

def makeVar(type,name,value) :
  tempStr = (compressListName(name))
  return(tempStr + ' = ' + value)
def getWord(wordIndex,sentance,type = 0) :
  try :
    index = 0
    index2 = 1
    inQuote = 0
    inBracket = 0
    temp = ''
    if(type == 1) :
      while(sentance[index] == ' ') :
        index = index + 1
    else :
      while(sentance[index] == ' ') :
        temp = temp + ' '
        index = index + 1
    while(index2 < wordIndex) :
      while((sentance[index] != ' ' and sentance[index] != ';') or inQuote == 1 or inBracket == 1) :
        if(sentance[index] == '"') :
          if(inQuote == 0) :
            inQuote = 1
          else :
            inQuote = 0
        if(sentance[index] == '(') :
          if(inBracket == 0) :
            inBracket = 1
        if(sentance[index] == ')') :
          if(inBracket == 1) :
            inBracket = 0
        index = index + 1
        if(index == len(sentance)) :
            break
      index = index + 1
      index2 = index2 + 1
    while((sentance[index] != ' ' and sentance[index] != ';') or inQuote == 1 or inBracket == 1) :
      if(sentance[index] == '"') :
        if(inQuote == 0) :
          inQuote = 1
        else :
          inQuote = 0
      if(sentance[index] == '(') :
        if(inBracket == 0) :
          inBracket = 1
      if(sentance[index] == ')') :
        if(inBracket == 1) :
          inBracket = 0
      temp = temp + sentance[index]
      index = index + 1
      if(index == len(sentance)) :
          break
    return temp
  except :
    print(bcolors.WARNING + "   SYNTAX ERROR: reached end of line and missing ';'")
    return ""
# open script
file = open("main.osr", "r")
cpp = open("run.cpp", "w")
cpp.write('#include "src/osr.h"\n#include "src/input.hpp"\n')
cpp = open("run.cpp", "a")
# int main(void) {\n
# process script
varList = []
loopType = 0;
for idx,line in enumerate(file) :
    # Debug print:
    #print(varList)
    #print(getWord(1,line,1) in varList)
    #print(getWord(1,line,1))
    #print(line)
  #try :
    if(getWord(1,line,1)[0] == "/" and getWord(1,line,1)[1] == "/") :
      pass
    elif(len(getWord(1,line,1)) > 2) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2]) == "def") :
      cpp.write("  " + getWord(2,line,1) + ' ' + getWord(3,line,1) + ' ' + getWord(4,line,1))
      varList.append(compressListName(getWord(2,line)))
    elif(len(getWord(1,line,1)) > 5) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4] + getWord(1,line,1)[5]) == "system") :
      cpp.write("  " + line)
    elif(len(getWord(1,line,1)) > 5) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4] + getWord(1,line,1)[5]) == "random") :
      cpp.write("  " + line)
    elif(len(getWord(1,line,1)) > 3) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3]) == "seed") :
      cpp.write("  " + getWord(1,line) + ";\n")
    elif(len(getWord(1,line,1)) > 1) and (getWord(1,line,1)[0] + getWord(1,line,1)[1]) == "if" :
      cpp.write("  " + line)
    elif(len(getWord(1,line,1)) > 2) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2]) == "int") :
      cpp.write("  " + line)
      varList.append(compressListName(getWord(2,line,1)))
    elif(len(getWord(1,line,1)) > 2) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2]) == "str") :
      cpp.write("  char* " + makeVar(getWord(1,line,1),getWord(2,line,1),getWord(4,line,1)) + ";\n")
      varList.append(compressListName(getWord(2,line,1)))
    elif(len(getWord(1,line,1)) > 3) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3]) == "char") :
      cpp.write("  char " + makeVar(getWord(1,line),getWord(2,line),getWord(4,line)) + ";\n")
      varList.append(compressListName(getWord(2,line,1)))
    elif(len(getWord(1,line,1)) > 4) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4]) == "print") :
      cpp.write("  " + getWord(1,line) + ";\n")
    elif(len(getWord(1,line,1)) > 4) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4]) == "delay") :
      cpp.write("  " + getWord(1,line) + ";\n")
    elif(len(getWord(1,line,1)) > 4) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4]) == "while") :
      cpp.write("  " + line)
    elif(len(getWord(1,line,1)) > 3) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3]) == "exit") :
      cpp.write("  " + getWord(1,line) + ";\n")
    elif(len(getWord(1,line,1)) > 5) and ((getWord(1,line,1)[0] + getWord(1,line,1)[1] + getWord(1,line,1)[2] + getWord(1,line,1)[3] + getWord(1,line,1)[4] + getWord(1,line,1)[5]) == "repeat") :
      repeatIdentity = 'i' + str(repeatI)
      temp = ""
      index1 = 0
      while(line[index1] != '(') :
        index1 = index1 + 1
      index1 = index1 + 1
      while(line[index1] != ')') :
        temp = temp + line[index1]
        index1 = index1 + 1
      index1 = 0;
      while(line[index1] == ' ') :
        cpp.write(' ')
        index1 = index1 + 1
      cpp.write("  for (int " + repeatIdentity + "=0; " + repeatIdentity + "<"+ str(temp) +"; ++" + repeatIdentity + ") {\n")
      repeatI = repeatI + 1
    elif(getWord(1,line,1) == '}'):
      cpp.write("  " + line)
    elif(getWord(1,line,1) == "clear()") :
      cpp.write("  " + line)
    # Stay at end to avoid error
    elif(compressListName(getWord(1,line,1)) in varList) :
      if((getWord(2,line,1) == "++")) :
        cpp.write("  " + getWord(1,line) + "++;\n")
      elif((getWord(1,line,1)[-1] == "]")) :
        if(getWord(1,line,1)[-1] == ']') :
          cpp.write("  " + line)
      else :
        cpp.write("  " + line)
    else :
      print(bcolors.FAIL + "   COMPILE FAILURE: line " + str(idx) + ': fuction "' + getWord(1,line,1) + '" not found')
      print(varList)
      print(compressListName(getWord(1,line,1)))
      exit("Compile failed due to code error")
  #except :
  #  print(bcolors.FAIL + "   COMPILE FAILURE: *line " + str(idx) + ': fuction "' + getWord(1,line) + '" not found')
  #  exit("Compile failed due to code error")
#cpp.write("}")