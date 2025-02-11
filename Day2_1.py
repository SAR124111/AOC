
def load_reports(file_path):

    with open(file_path, 'r') as file:

        reports = [line.strip() for line in file]

    return reports


def is_safe(report):

    report = list(map(int, report.split()))


    sorted_report = sorted(report)

    if report == sorted_report or report == sorted_report[::-1]:

        for i in range(1, len(report)):

            if abs(report[i] - report[i - 1]) > 3 or report[i] == report[i - 1]:

                return False

        return True

    return False


# Path to the input file

file_path = 'day2.txt'


# Load reports from the file

reports = load_reports(file_path)


# Evaluate the reports

safe_reports = sum(is_safe(report) for report in reports)


print("Solution 1:", safe_reports)