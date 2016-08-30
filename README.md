# Robotics-AI
This repository is about some basic Python codes implemented according to Sesbian's class. Different form resources provided by the class, here I put some different codes wrote by my own, but most of them are same. Secondly, I will put the notes for each important code lines. At last , I plan to write a blog about the calss, to explain main ideas in each chapter, which will be update later.

---
## Contents
[TOC]

---
## Localization
This part refers to codes implemented in folder ==*Chapter1-Localization*==.
Localization is very important for robots. Because if you can't estimate its
position acctuately, then it's impossible for it to do planning or even high
level work. Solving localization problem mainly covers two steps: *sense &
move*. Every step you sense, you get information from environment, then you will get a more reliable position estimate. But when you move, you lost information,	cause uncertainty. So codes in this chapter mainly include two functions:	*sense(), move()*. I put some easy programs together to get a mor
inherented function, which is different with step by step coding in class.
Functions in this chapter include:

* pHit_pMiss
* sense()
* exact_motion()
* inexact_motion()
* sense_move()

