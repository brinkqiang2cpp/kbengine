# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 
from skills.base.SkillInitiative import SkillInitiative

class SkillAttack(SkillInitiative):
	def __init__(self):
		SkillInitiative.__init__(self)

	def canUse(self, caster, receiver):
		"""
		virtual method.
		可否使用 
		@param caster: 使用技能者
		@param receiver: 受技能影响者
		"""
		return True
		
	def use(self, caster, receiver):
		"""
		virtual method.
		使用技能
		@param caster: 使用技能者
		@param receiver: 受技能影响者
		"""
		pass