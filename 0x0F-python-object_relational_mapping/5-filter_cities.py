#!/usr/bin/python3
"""
Script that takes name of state as argument and lists all cities in that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """script should take 4 arguments"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                    ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
