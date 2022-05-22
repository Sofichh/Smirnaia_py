class Students:

    def __init__(self, surnamename, numofgroup, ac_perf):
        self.surnamename = surnamename
        self.numofgroup = numofgroup
        self.ac_perf = ac_perf

    def av_score(self):
        av = sum(self.ac_perf) / 5
        return av

