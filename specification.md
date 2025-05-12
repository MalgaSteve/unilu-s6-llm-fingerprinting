# Specification: Model Identification

Meireles Lopes Steve
version 0.1

## Introduction
This document describes the plan for my BSP S6 with the title "Recognizing and
Attacking Chatbot Models through Specific Queries". 

The intended readers are the developer and the tutor of this project. This
document will include system functionality of the project, the scope of the
project and use cases.

## Overview

Nowadays, chatbots run on Large Language Models (LLMs) and are increasingly
used, causing new openings for attacks. This project answers the question:
”What are the minimal queries to identify the model used?”. This will be done
by quering and comparing n-numbers of LLMs, analyzing their results, and
identifying their individual differences. We deduct signatures to find the
minimal set of queries for a set of given LLMs. 

The software will not have a graphical user interface but will be useable on a
UNIX-terminal.

### Users
Everyone.

### Functionality

- the user should be able to identify a model 
- the user should be able to direct a follow-up attack exploiting the
  vulnerabilities of the identified model

## Platform
It will be launched as a python executable. Only tested in a UNIX environnment.

## Goals and Scopes

- the program should be able to randomly query open-source LLMs
- should be able to compare based on the answers given by the LLMs after being
  queried
- 
## Deliverables
## Technical Process
