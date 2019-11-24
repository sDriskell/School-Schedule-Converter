

class Student:
    def __init__(self):
        self.fname = None
        self.lname = None

        self.iep = None
        self.eval = None
        self.reval = None
        self.aod = None
        self.testdate = None
        self.evaldate = None

    #getters
    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_iep(self):
        return self.iep

    def get_eval(self):
        return self.eval

    def get_reval(self):
        return self.reval

    def get_aod(self):
        return self.aod

    def get_testdate(self):
        return self.testdate

    def get_evaldate(self):
        return self.testdate

    #setters
    def set_fname(self, name):
        self.fname = name

    def set_lname(self, name):
        self.lname = name

    def set_iep(self, iep: float):
        self.iep = iep

    def set_eval(self, iep: float):
        self.eval = eval

    def set_reval(self, reval: float):
        self.reval = reval

    def set_aod(self, aod: float):
        self.aod = aod

    def set_testdate(self, testdate: float):
        self.testdate = testdate

    def set_evaldate(self, evaldate: float):
        self.evaldate = evaldate
