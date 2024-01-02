#!/usr/bin/env python

from cleaning_robot import CleaningRobot


def main():
    test_failed = False
    # TODO - initiate cleaning robot and test what happens when it encounters
    # an inner door, the main door or a prison guard. Then modify cleaning_robot.py
    # so that it works accordingly.

    cleaning_robot = CleaningRobot(True)

    inner_door = cleaning_robot.when_encounter_inner_door()
    main_door = cleaning_robot.when_encounter_outer_door()
    prison_guard = cleaning_robot.when_encounter_guard()


    if inner_door != "Door unlocked.\nDoor entered.\n":
        test_failed = True

    if main_door != "Door unlocked.\nTurn around.\n":
        test_failed = True

    if prison_guard != "":
        test_failed = True

    if test_failed:
        print("Unfortunately, one or several tests failed.")
    else:
        print("All tests ran successfully.")


if __name__ == "__main__":
    main()
