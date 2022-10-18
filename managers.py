class Action_Manager:
	def __init__(self):
		super(Action_Manager, self).__init__()
		self._actions = {}
		self._vars = {}


	@property
	def vars(self):
		return self._vars


	def get(self, label):
		return self._vars.get(label)


	def set(self, label, value):
		self._vars[label] = value


	def extendModule(self, module):
	for name, val in module.__dict__.items():
		if callable(val): self.extend(label=name, action=val)


	def extend(self, label, action):
		self._actions[label] = action


	def execute(self, label, data):
		action = self._actions.get(label)
		if action: return action(self, data)
