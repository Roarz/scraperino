import unittest
import module1
from onlineList import get_online_list, filter_players
from sendCharInfo import check_player

class TestStringMethods(unittest.TestCase):
    def test_get_online_list(self):
        print("online list: %s" % len(onlineList))
        self.assertGreater(len(onlineList),50)

    def test_targets(self):
        targets = filter_players(onlineList, minLvl=minLvl, maxLvl=maxLvl)
        print("targets: %s" % len(targets))
        self.assertGreater(len(targets),1)

    def test_highest_player(self):
        targets = filter_players(onlineList, minLvl=minLvl, maxLvl=maxLvl)
        highestPlayer = targets[len(targets) -1]
        highest = highestPlayer.level
        print("highest: %s" % highestPlayer.name, "(%s)" % highestPlayer.level, highestPlayer.vocation)
        self.assertLessEqual(highest, maxLvl)

    def test_lowest_player(self):
        targets = filter_players(onlineList, minLvl=minLvl, maxLvl=maxLvl)
        lowest = targets[0].level
        print("lowest: %s" % targets[0].name, "(%s)" % targets[0].level, targets[0].vocation)
        self.assertGreaterEqual(lowest, minLvl)

    def test_find_targets(self):
        targets = filter_players(onlineList, minLvl=minLvl, maxLvl=maxLvl)
        for target in targets:
            print("target: %s" % target.name)
            check_player(target.name)
            break
        self.assertGreater(len(targets),1)

minLvl = 60
maxLvl = 90
onlineList = get_online_list("Wintera")

if __name__ == '__main__':
    unittest.main()