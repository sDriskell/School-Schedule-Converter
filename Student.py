class Student:

    # Default constructor
    def __init__(self):
        self.fName = None
        self.lName = None

        self.iep = None
        self.eval = None
        self.reval = None
        self.aod = None
        self.testdate = None
        self.evaldate = None

    #
    def __init__(self, fName, lName, iep, eval, reval, aod, testdate, evaldate ):
        self.fName = fName
        self.lName = lName

        self.iep = iep
        self.eval = eval
        self.reval = reval
        self.aod = aod
        self.testdate = testdate
        self.evaldate = evaldate

    # Utility function
    def toString(self):
        print(self.fName)

    #  getters
    def get_fName(self):
        return self.fName

    def get_lName(self):
        return self.lName

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
    def set_fName(self, name):
        self.fName = name

    def set_lName(self, name):
        self.lName = name

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
