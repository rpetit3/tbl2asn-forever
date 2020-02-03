#! /usr/bin/env python3
"""
Change the date in tbl2asn-forever SQN output to the current date.

This will update the date if it is set to January, 1st 2019. Otherwise, the date will be left intact.
"""
from datetime import datetime
PROGRAM="fix-sqn-date"
VERSION="25.7.1f"
TODAYS_DATE=datetime.now()
DAY=TODAYS_DATE.strftime("%-d")
MONTH=TODAYS_DATE.strftime("%-m")
YEAR=TODAYS_DATE.strftime("%Y")
MONTH_FORMAT='str "month" ,\n              data\n                int {0} }} ,\n'
DAY_FORMAT='str "day" ,\n              data\n                int {0} }} ,\n'
YEAR_FORMAT='str "year" ,\n              data\n                int {0} }} }} }} ,\n'
CREATE_FORMAT='create-date\n          std {{\n            year {0} ,\n            month {1} ,\n            day {2} }} }} ,\n'

if __name__ == '__main__':
    import argparse as ap
    import sys

    parser = ap.ArgumentParser(
        prog=PROGRAM,
        conflict_handler='resolve',
        description=f'{PROGRAM} (v{VERSION}) - Change date in SQN to the currrent date.'
    )
    parser.add_argument('sqn', metavar="SQN", type=str,
                        help='Input SQN file to change date')
    parser.add_argument('--version', action='version',
                        version=f'{PROGRAM} {VERSION}')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    sqn_text = None
    with open(args.sqn, 'rt') as sqn_fh:
        sqn_text = "".join(sqn_fh.readlines())
    sqn_text = sqn_text.replace(MONTH_FORMAT.format('1'), MONTH_FORMAT.format(MONTH))
    sqn_text = sqn_text.replace(DAY_FORMAT.format('1'), DAY_FORMAT.format(DAY))
    sqn_text = sqn_text.replace(YEAR_FORMAT.format('2019'), YEAR_FORMAT.format(YEAR))
    sqn_text = sqn_text.replace(CREATE_FORMAT.format('2019', '1', '1'), CREATE_FORMAT.format(YEAR, MONTH, DAY))

    print(sqn_text.rstrip())
