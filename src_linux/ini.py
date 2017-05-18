import CodeForces
import AtCoder

contestJudge = sys.argv[1]
contestId = sys.argv[2]

if contestJudge == "CodeForces":
	CodeForces.doParsing(contestId)
else if contestJudge == "AtCoder":
	AtCoder.doParsing(contestId)
else:
	print "Judge not recognized"
