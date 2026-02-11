def main_main_menu():
    try:
        while True:
            print("="*69)
            print(f"1. Admin\n"
                  f"2. Teacher\n"
                  f"3. Staff\n"
                  f"4. Student\n"
                  f"5. Exit")
            print("="*69)
            choice = input("Enter your choice: ")
            if choice == '1':
                login_admin()
            elif choice == '2':
                teacher_portal()
            elif choice == '3':
                login_staff()
            elif choice == '4':
                menu_student()
            elif choice == '5':
                print("Thank you for using me :D ")
                exit()
    except ValueError:
        print("Invalid input")

def login_admin():
    admin_users, admin_passwords = read_csv("admin.csv")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in admin_users:
            index = admin_users.index(username)
            if admin_passwords[index] == password:
                print("Sign-in successful!")
                menu_admin()
                break
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")

def menu_admin():
    while True:
        print("=" * 69)
        print(f"1. Manage User Accounts"
              f"\n2. Student Management"
              f"\n3. Manage courses offerings"
              f"\n4. Class Schedule"
              f"\n5. Report Generation for students"
              f"\n6. Report Generation for institution"
              f"\n7. Update resource allocation"
              f"\n8. Exit")
        print("=" * 69)
        choice = input("enter (1-8): ")
        if choice not in ['1','2','3','4','5','6','7','8']:
            print("please enter a number (1-8)")
        if choice == '1':
            main()
        elif choice == '2':
            student_management()
        elif choice == '3':
            read_course_management()
            manage_courses()
        elif choice == '4':
            class_schedule_menu()
        elif choice == '5':
            records = read_csv_stu_management()
            read_csv_report_gen(records)
            report_generation(records)
        elif choice == '6':
            read_inst()
            rg_institution()
        elif choice == '7':
            update_res()
        elif choice == '8':
            break

def read_csv(filename):
    users, passwords = [], []
    try:
        with open(filename, "r") as file:
            for line in file:
                user, password = line.strip().split(",")
                users.append(user)
                passwords.append(password)
    except FileNotFoundError:
        pass
    return users, passwords

def save_to_csv(filename, users, passwords):
    with open(filename, "w") as file:
        for i in range(len(users)):
            file.write(f"{users[i]},{passwords[i]}\n")

def add_user(username, password, users, passwords, filename):
    users.append(username)
    passwords.append(password)
    save_to_csv(filename, users, passwords)
    return users, passwords

def delete_user(username, password, users, passwords, filename):
    if username in users:
        index = users.index(username)
        if passwords[index] == password:
            del users[index]
            del passwords[index]
            save_to_csv(filename, users, passwords)
            return users, passwords, "Account deleted successfully!"
        else:
            return users, passwords, "Incorrect password."
    return users, passwords, "Username not found."

def change_password(username, old_password, new_password, users, passwords, filename):
    if username in users:
        index = users.index(username)
        if passwords[index] == old_password:
            passwords[index] = new_password
            save_to_csv(filename, users, passwords)
            return users, passwords, "Password changed successfully!"
        else:
            return users, passwords, "Incorrect old password."
    return users, passwords, "Username not found."

def manage_accounts(users, passwords, filename):
    while True:
        print("=" * 69)
        print("1. Create an account\n2. Delete an account\n3. Change password\n4. Exit")
        choice = input("Choose an option (1-4): ")
        print("=" * 69)

        if choice == '1': # create acc
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            users, passwords = add_user(username, password, users, passwords, filename)
            print("Account created successfully!")

        elif choice == '2': # del acc
            username = input("Enter username to delete: ")
            password = input("Enter password: ")
            users, passwords, message = delete_user(username, password, users, passwords, filename)
            print(message)

        elif choice == '3': # change pass
            username = input("Enter your username: ")
            old_password = input("Enter your current password: ")
            new_password = input("Enter your new password: ")
            users, passwords, message = change_password(username, old_password, new_password, users, passwords, filename)
            print(message)

        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")
    return users, passwords

def main():
    students_file = "students.csv"
    teachers_file = "teachers.csv"
    staff_file = "staff.csv"
    admin_file = "admin.csv"

    student_users, student_passwords = read_csv(students_file) # read files to compare
    teacher_users, teacher_passwords = read_csv(teachers_file)
    staff_users, staff_passwords = read_csv(staff_file)
    admin_users, admin_passwords = read_csv(admin_file)

    while True:
        print("=" * 69)
        print("1. Manage Student Accounts\n2. Manage Teacher Accounts\n3. Manage Staff Accounts\n4. Manage Admin Accounts\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            student_users, student_passwords = manage_accounts(student_users, student_passwords, students_file) # need to assign variables
        elif choice == '2':
            teacher_users, teacher_passwords = manage_accounts(teacher_users, teacher_passwords, teachers_file)
        elif choice == '3':
            staff_users, staff_passwords = manage_accounts(staff_users, staff_passwords, staff_file)
        elif choice == '4':
            admin_users, admin_passwords = manage_accounts(admin_users, admin_passwords, admin_file)
        elif choice == '5':
            print("back to admin menu")
            break
        else:
            print("Invalid option. Try again.")

def read_csv_stu_management():
    records = {}
    try:
        with open("student_record.csv", "r") as read_file_stu_management:
            for line in read_file_stu_management:
                stu_name, e_status, a_performance, p_details = line.strip().split(", ")
                records[stu_name] = {
                    'Enrolment status': e_status,
                    'Academic performance': a_performance,
                    'Personal details': p_details
                }
    except FileNotFoundError:
        pass
    return records

def save_csv_stu_management(records):
    with open("student_record.csv", "w") as save_stu_management:
        for stu_name, details in records.items():
            save_stu_management.write(f"{stu_name}, "
                       f"{details['Enrolment status']}, "
                       f"{details['Academic performance']}, "
                       f"{details['Personal details']}\n")

def student_management():
    records = read_csv_stu_management() # read the data in file dulu

    while True:
        print("=" * 69)
        print(f"1. Create student record "
              f"\n2. View student records "
              f"\n3. Back to admin menu ")
        print("=" * 69)
        choice = input("Key in choice: ")

        if choice == '1':
            stu_name = input("Enter student's name: ")
            e_status = input("Key in enrolment status: ")
            a_performance = input("Key in academic performance: ")
            p_details = input("Key in personal details: ")
            records[stu_name] = { # assign values
                'Enrolment status': e_status,
                'Academic performance': a_performance,
                'Personal details': p_details
            }
            save_csv_stu_management(records)
            print(f"Records for {stu_name} have been saved! ")

        elif choice == '2': # view
            stu_name = input("Enter student's name to view record: ")

            if stu_name in records:
                print("\n--- Student Record ---")
                print(f"Enrolment status: {records[stu_name]['Enrolment status']}")
                print(f"Academic performance (CGPA): {records[stu_name]['Academic performance']}")
                print(f"Personal details: {records[stu_name]['Personal details']}")
            else:
                print(f"No record found for {stu_name} ")

        elif choice == '3':
            print("Thank you for using student management ")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

def read_course_management():
    courses = {}
    try:
        with open("available_courses.csv", "r") as r_course_mge:
            lines = r_course_mge.readlines()
            if len(lines) <= 1:  # Skip head
                return courses

            for line in lines[1:]: # sec row onwards
                info = [i.strip() for i in line.strip().split(",")]

                if len(info) >= 2:
                    courses[info[0]] = {
                        "duration": info[1],
                        "instructor": info[2] if len(info) > 2 else "" # blank if ins mty
                    }
    except FileNotFoundError:
        pass
    return courses

def save_course_management(courses):
    with open("available_courses.csv", "w") as file:
        file.write("Course Name,Duration,Instructor\n")
        for course_name, details in courses.items():
            duration = details['duration']
            instructor = details.get('instructor', "") # avoid error if don hv ins
            file.write(f"{course_name},{duration},{instructor}\n")

def manage_courses():
    courses = read_course_management()
    while True:
        try:
            print("=" * 69)
            print(f"1. Create course offerings"
                  f"\n2. Update course offerings"
                  f"\n3. Delete course offerings"
                  f"\n4. Assign instructor to course"
                  f"\n5. Back to admin menu")
            print("=" * 69)
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                c_offer = input("Enter the course to be created: ")
                c_duration = input("Enter the duration of the course in years/units: ")
                if c_offer not in courses:
                    courses[c_offer] = {'duration': c_duration}
                    save_course_management(courses)
                    print(f"Course '{c_offer}' added!")

            elif choice == '2':
                u_offer = input("Enter the course you want to update: ")
                if u_offer in courses:
                    new_duration = input("Enter the new duration for the course: ")
                    courses[u_offer]['duration'] = new_duration # replace new
                    save_course_management(courses)
                    print(f"Course '{u_offer}' updated successfully!")
                else:
                    print("Course not found, please re-enter")

            elif choice == '3':
                del_offer = input("Enter the course to be deleted: ")
                if del_offer in courses:
                    del courses[del_offer]
                    save_course_management(courses)
                    print(f"Course '{del_offer}' deleted successfully!")
                else:
                    print("Course not found, please re-enter")

            elif choice == '4':
                course_name = input("Enter the course to assign an instructor: ")
                if course_name in courses:
                    ins_assigned = [details["instructor"] for details in courses.values() if "instructor" in details] # check ins name used
                    ins = input("Enter the instructor's name: ")
                    if ins not in ins_assigned:
                        courses[course_name]["instructor"] = ins
                        save_course_management(courses)
                        print(f"Instructor '{ins}' assigned to course '{course_name}'.")
                else:
                    print("Course not found, please re-enter")

            elif choice == '5':
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def read_s_timetable_csv():
    class_schedule = []

    with open("S-timetable.csv", "r") as read_timetable:
        for line in read_timetable:
            data = line.strip().split(",")
            if len(data) == 6:
                student = {
                    "name": data[0],
                    "tp number": data[1],
                    "week number": data[2],
                    "class": data[3],
                    "day": data[4],
                    "time frame": data[5]
                }
                class_schedule.append(student)
    return class_schedule

def overlapping_entries(timetable): # check for any overlap
    overlaps = []
    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):
            if (timetable[i]["week number"] == timetable[j]["week number"] and
                    timetable[i]["day"] == timetable[j]["day"]):
                start1, end1 = convert_to_minutes(timetable[i]["time frame"]) # 1st row overlap
                start2, end2 = convert_to_minutes(timetable[j]["time frame"]) # 2nd row overlap
                if start1 < end2 and start2 < end1: # start1 earlier sec end2, start2 later start1
                    overlaps.append((i, j))
    return overlaps

def convert_to_minutes(time_range): # differentiate start and end
    start, end = time_range.split("-")
    return to_minutes(start), to_minutes(end)

def to_minutes(time_str):
    h = int(time_str[:-2])
    m = int(time_str[-2:])
    return h * 60 + m

def save_s_timetable_csv(timetable):
    with open("S-timetable.csv", "w") as save_timetable:
        for entry in timetable:
            line = f"{entry['name']},{entry['tp number']},{entry['week number']},{entry['class']},{entry['day']},{entry['time frame']}\n"
            save_timetable.write(line)

def show_timetable():
    timetable = read_s_timetable_csv()
    if not timetable:
        print("No data in timetable yet :c")
    else:
        print("\nCurrent class schedule:")
        for i, entry in enumerate(timetable): # assign with number of rows
            print(f"Row {i + 1}: Name:{entry['name']}, TP number:{entry['tp number']}, Week:{entry['week number']}, "
                  f"Class:{entry['class']}, Day:{entry['day']}, Time frame:{entry['time frame']}")

def fix_overlap():
    timetable = read_s_timetable_csv()
    overlaps = overlapping_entries(timetable)

    if not overlaps:
        print("No overlaps found.")
        return
    else:
        while overlaps:
            print("\nOverlapping classes found:")
            for row1, row2 in overlaps:
                print(f"Conflict: Row {row1 + 1} and Row {row2 + 1} -> {timetable[row1]['class']} ({timetable[row1]['time frame']}) "
                      f"overlaps with {timetable[row2]['class']} ({timetable[row2]['time frame']})")
            row_to_update = int(input("\nEnter the row number you want to update (or 0 to exit): ")) - 1
            if row_to_update < 0:
                print("Exiting without resolving overlaps")
                return

            if row_to_update < len(timetable):
                new_week = input("Enter a new week number: ")
                new_day = input("Enter a new day (e.g., MON, TUE, WED, THU, FRI): ")
                new_time_frame = input("Enter a new time frame (e.g., 1000-1300): ")
                timetable[row_to_update]["week number"] = new_week # replace new time
                timetable[row_to_update]["day"] = new_day
                timetable[row_to_update]["time frame"] = new_time_frame
                save_s_timetable_csv(timetable)
                print("Schedule updated")
            else:
                print("Invalid row selection. Please re-enter.")

            timetable = read_s_timetable_csv()
            overlaps = overlapping_entries(timetable)

def add_class_schedule():
    timetable = read_s_timetable_csv()
    show_timetable()
    new_info = {
        "name": input("Enter student name: "),
        "tp number": input("Enter student ID: "),
        "week number": input("Enter week: "),
        "class": input("Enter subject: "),
        "day": input("Enter day (e.g., MON, TUE, WED, THU, FRI): "),
        "time frame": input("Enter military time range (e.g., 1000-1300): ")
    }
    overlapping_rows = overlapping_entries(timetable) # check overlap
    if overlapping_rows:
        print("Overlap detected. Please enter another time.")
        fix_overlap()
    else:
        timetable.append(new_info)
        save_s_timetable_csv(timetable)
        print("Class added.")

def update_class():
    timetable = read_s_timetable_csv()
    show_timetable()
    try:
        up_row = int(input("Enter the row number of the class to update (or 0 to cancel): ")) - 1
        if up_row < 0:
            print("Update cancelled.")
            return
        if up_row >= len(timetable):
            print("Invalid selection. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    print("\nCurrent details for the selected row:")
    selected_entry = timetable[up_row]
    print(
        f"Name: {selected_entry['name']}, TP number: {selected_entry['tp number']}, Week: {selected_entry['week number']}, "
        f"Class: {selected_entry['class']}, Day: {selected_entry['day']}, Time frame: {selected_entry['time frame']}")

    print("\nEnter new details for the selected row:")
    new_info = {
        "name": input("Enter new student name: "),
        "tp number": input("Enter new student ID: "),
        "week number": input("Enter new week: "),
        "class": input("Enter new subject: "),
        "day": input("Enter new day (e.g., MON, TUE, WED, THU, FRI): "),
        "time frame": input("Enter new time frame (e.g., 1000-1300): ")
    }
    timetable[up_row] = new_info
    overlaps = overlapping_entries(timetable)  # Check for overlaps
    if overlaps:
        print("\nWarning: The updated schedule causes an overlap!")
        fix_overlap()
    else:
        save_s_timetable_csv(timetable)
        print("\nSchedule updated successfully!")

def class_schedule_menu():
    while True:
        print("=" * 69)
        print("enter\n1. check any existing overlapping\n2. add new class schedule\n3. Update class schedule\n4. Back to admin menu")
        print("=" * 69)
        choice = input("enter you choice: ")
        if choice == '1':
            fix_overlap()
        elif choice == '2':
            add_class_schedule()
        elif choice == '3':
            update_class()
        elif choice == '4':
            break
        else:
             print("invalid input")

def save_csv_report_gen(stu_name, attendance, financial_report):
    with open("report_generation.csv", "a") as save_report_gen:
        save_report_gen.write(f"{stu_name}, {attendance}, {financial_report}\n")

def read_csv_report_gen(records):
    try:
        with open("report_generation.csv", "r") as read_report_gen:
            for line in read_report_gen:
                stu_name, attendance, financial_report = line.strip().split(", ")
                if stu_name in records:
                    records[stu_name]['Attendance'] = attendance
                    records[stu_name]['Financial Report'] = financial_report
    except FileNotFoundError:
        print("No saved reports yet :D ")

def report_generation(records):
    while True:
        print("=" * 69)
        print("Choose an option: "
              "\n 1. View All Student Reports "
              "\n 2. Add/Update Student Report "
              "\n 3. Back to main menu ")
        print("=" * 69)
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            print("=" * 69)
            print(
                f"{'Student Name':<20} {'Academic Performance':<20} {'Attendance':<15} {'Financial Report(RM total fees,amount payed,remaining fees)':<20}")
            print("=" * 69)
            for stu, details in records.items():
                print(
                    f"{stu:<20} {details['Academic performance']:<20} {details['Attendance']:<15} {details['Financial Report']:<20}")
            print("=" * 69)

        elif choice == '2':
            stu_name = input("Enter student name: ")
            if stu_name not in records:
                print(f"No records found for {stu_name}. Please add the student in Student Management first.")
                continue

            while True:
                print("=" * 69)
                print("Generate Reports: "
                      "\n 1. Academic Performance "
                      "\n 2. Attendance "
                      "\n 3. Financial Reports "
                      "\n 4. Back to previous menu ")
                print("=" * 69)
                choice = input("Enter choice (1-4): ")

                if choice == '1':
                    print(f"Academic Performance: {records[stu_name]['Academic performance']}")
                    new_performance = input("Enter updated academic performance: ")
                    records[stu_name]['Academic performance'] = new_performance
                    save_csv_stu_management(records)
                    print("Academic Performance updated")

                elif choice == '2':
                    try:
                        d_came = int(input(f"Enter the number of days {stu_name} attended class: "))
                        total_d = int(input(f"Enter the total number of class days: "))

                        if total_d == 0:
                            print("Error: Total number of class days cannot be zero.")
                        else:
                            attendance_rate = (d_came / total_d) * 100
                            print(f"{stu_name} attended {d_came} days out of {total_d} days.")
                            print(f"Their attendance rate is {attendance_rate:.2f}%.")
                            records[stu_name]['Attendance'] = f"{attendance_rate:.2f}%"
                            save_csv_report_gen(stu_name, records[stu_name]['Attendance'],
                                                records[stu_name].get('Financial Report', 'N/A'))
                            print("Attendance updated")

                    except ValueError:
                        print("Invalid input. Please number values for attendance.")

                elif choice == '3':
                    try:
                        sum_cost = int(input("Enter the total cost for studying: "))
                        payed_cost = int(input("Enter the payment you made: "))

                        if payed_cost > sum_cost:
                            print("Error: Payment cannot exceed the total cost.")
                        else:
                            bal_cost = sum_cost - payed_cost
                            print(f"{stu_name} still needs to pay RM{bal_cost} to clear their fees.")
                            financial_report = f"{sum_cost},{payed_cost},{bal_cost}"
                            records[stu_name]['Financial Report'] = financial_report
                            save_csv_report_gen(stu_name, records[stu_name].get('Attendance', 'N/A'), financial_report)
                            print("Financial Report updated")

                    except ValueError:
                        print("Invalid input! Please enter number.")

                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please re-enter.")

        elif choice == '3':
            print("Thanks for using me :p CYA next time ")
            break
        else:
            print("Invalid choice. Please re-enter.")


def read_inst():
    institution = {}
    try:
        with open("institution.csv", 'r') as read:
            lines = read.readlines()
            if len(lines) <= 1:
                print("No institution records found.")
                return institution

            for line in lines[1:]:
                data = line.strip().split(",")
                if len(data) == 4:
                    institution[data[0]] = {
                        "ap_inst": data[1],
                        "att_inst": data[2],
                        "f_inst": data[3]
                    }
    except FileNotFoundError:
        print("No institution reports found.")
    return institution

def save_inst(institution):
    with open("institution.csv", 'w') as save:
        save.write("Year,Avg_GPA,Avg_Attendance,Total_Tuition\n")
        for year, details in institution.items():
            save.write(f"{year},{details['ap_inst']},{details['att_inst']},{details['f_inst']}\n")

def rg_institution():
    institution = read_inst()
    while True:
        print("=" * 69)
        print("1. Enter/Update Institution Report")
        print("2. View Institution Reports")
        print("3. Back to Admin Menu")
        print("=" * 69)
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            yr = input("Enter the year for the report: ")
            if yr in institution:
                print(f"Report for {yr} already exists. Updating the record.")

            ap_institution = input("Enter the average GPA of the institution this year: ")
            att_institution = input("Enter the average attendance of the institution this year: ")
            f_institution = input("Enter the total tuition fee collected this year: ")
            institution[yr] = {
                "ap_inst": ap_institution,
                "att_inst": att_institution,
                "f_inst": f_institution
            }
            save_inst(institution)
            print(f"Report for {yr} saved")

        elif choice == '2':  # View Reports
            if not institution:
                print("No reports available.")
            else:
                print("=" * 69)
                print(f"{'Year':<10} {'Average GPA':<20} {'Attendance Rate':<20} {'Total Tuition Collected':<20}")
                print("=" * 69)

                for yr, details in institution.items():
                    print(f"{yr:<10} {details['ap_inst']:<20} {details['att_inst']:<20} {details['f_inst']:<20}")
                print("=" * 69)

        elif choice == '3':
            print("Thanks for using report generation for institution")
            break
        else:
            print("Invalid input. Please re-enter")


def read_update_res():
    resources = []

    with open("resources.csv", "r") as read_res:
        for line in read_res:
            data = line.strip().split(",")
            if len(data) == 6:
                name = {
                    'name': data[0],
                    'student/teacher': data[1],
                    'id': data[2],
                    'resource name': data[3],
                    'timeslot': data[4],
                    'class': data[5]
                }
                resources.append(name)
    return resources

def save_res(resources):
    with open("resources.csv", "w") as sv_res:
        for data in resources:
            line = f"{data['name']},{data['student/teacher']},{data['id']},{data['resource name']},{data['timeslot']},{data['class']}\n"
            sv_res.write(line)

def show_resources():
    resources = read_update_res()
    if not resources:
        print("No resource allocations yet :c")
    else:
        print("\nCurrent resource allocations:")
        for i, data in enumerate(resources):  # Assign with row numbers
            print(f"Row {i + 1}: Name: {data['name']}, Role: {data['student/teacher']}, ID: {data['id']}, "
                  f"Resource: {data['resource name']}, Timeslot: {data['timeslot']}, Class: {data['class']}")

def update_res():
    resources = read_update_res()
    show_resources()

    try:
        up_row = int(input("Enter the row number of the resource to update (or 0 to cancel): ")) - 1
        if up_row < 0:
            print("Update cancelled.")
            return
        if up_row >= len(resources):
            print("Invalid selection. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nCurrent details for the selected row:")
    selected_entry = resources[up_row]
    print(
        f"Name: {selected_entry['name']}, Role: {selected_entry['student/teacher']}, ID: {selected_entry['id']}, "
        f"Resource: {selected_entry['resource name']}, Timeslot: {selected_entry['timeslot']}, Class: {selected_entry['class']}"
    )

    print("\nEnter new details for the selected row:")
    new_info = {
        "name": input("Enter new name: "),
        "student/teacher": input("Enter role (Student/Teacher): "),
        "id": input("Enter new ID: "),
        "resource name": input("Enter new resource name: "),
        "timeslot": input("Enter new timeslot (e.g., Mon 5/2/2025 9:00-10:00): "),
        "class": input("Enter new class: ")
    }

    resources[up_row] = new_info
    save_res(resources)
    print("\nResource allocation updated successfully!")


def load_data(student_file, enrollment_file, teacher_file, lessons_file, grades_file, timetable_file, event_file, available_courses_file):
    data = {"students": [], "teachers": {}, "lessons": {}, "grades": [], "timetable": [], "events": {}, "available_courses": []}
    enrollments = {}
    try:
        with open(available_courses_file, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        if lines:
            data["available_courses"] = [line.split(',')[0].strip() for line in lines[1:]]
    except FileNotFoundError:
        print(f"Error: {available_courses_file} not found!")
    try:
        with open(enrollment_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    student_name, course = parts[:2]
                    enrollments.setdefault(student_name, []).append(course)
    except FileNotFoundError:
        print(f"Error: {enrollment_file} not found!")
    try:
        with open(student_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            student = {headers[i]: values[i] if i < len(values) else '' for i in range(len(headers))}
            student['Courses'] = ';'.join(enrollments.get(student['username'], []))
            data["students"].append(student)
    except FileNotFoundError:
        print(f"Error: {student_file} not found!")
    try:
        with open(teacher_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = [h.strip().lower() for h in lines[0].split(',')]
        if "subject" in headers and "name" in headers:
            subject_index, name_index = headers.index("subject"), headers.index("name")
            for line in lines[1:]:
                values = [v.strip() for v in line.split(',')]
                if len(values) > max(subject_index, name_index):
                    data["teachers"][values[subject_index].strip().lower()] = values[name_index].strip()
        else:
            print(f"Error: Incorrect headers in {teacher_file}")
    except FileNotFoundError:
        print(f"Error: {teacher_file} not found!")
    try:
        with open(lessons_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            course_name = values[0].strip()
            lesson_entry = {headers[i]: values[i].strip() for i in range(len(headers))}
            data["lessons"].setdefault(course_name, []).append(lesson_entry)
    except FileNotFoundError:
        print(f"Error: {lessons_file} not found!")
    try:
        with open(grades_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            data["grades"].append({headers[i]: values[i] if i < len(values) else '' for i in range(len(headers))})
    except FileNotFoundError:
        print(f"Error: {grades_file} not found!")
    try:
        with open(timetable_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = [h.strip() for h in lines[0].split(',')]
        for line in lines[1:]:
            values = line.split(',')
            data["timetable"].append({headers[i]: values[i].strip() if i < len(values) else '' for i in range(len(headers))})
    except FileNotFoundError:
        print(f"Error: {timetable_file} not found!")
    try:
        with open(event_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = [h.strip().lower() for h in lines[0].split(',')]
        required_headers = {"event name", "date", "day", "time", "student_name"}
        if not required_headers.issubset(set(headers)):
            print(f"Error: Incorrect headers in {event_file}")
            return data
        event_name_idx, date_idx, day_idx, time_idx, student_name_idx = headers.index("event name"), headers.index("date"), headers.index("day"), headers.index("time"), headers.index("student_name")
        for line in lines[1
        :]:
            values = [v.strip() for v in line.split(',')]
            if len(values) <= max(event_name_idx, date_idx, day_idx, time_idx, student_name_idx):
                continue
            student_name = values[student_name_idx].strip().lower()
            event_entry = {"event name": values[event_name_idx], "date": values[date_idx], "day": values[day_idx], "time": values[time_idx]}
            data["events"].setdefault(student_name, []).append(event_entry)
    except FileNotFoundError:
        print(f"Error: {event_file} not found!")
    return data

def merge_student_data(student_file, student_info_file):
    students = {}
    try:
        with open(student_info_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        headers = lines[0].split(',')
        for line in lines[1:]:
            values = line.split(',')
            username = values[0].strip()
            students[username] = values
    except FileNotFoundError:
        print(f"Error: {student_info_file} not found!")
        return
    try:
        with open(student_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    username, password = parts[0].strip(), parts[1].strip()
                    if username not in students:
                        students[username] = [username, password, "Unknown", "Unknown", "Unknown", "Unknown", "Unknown"]
    except FileNotFoundError:
        print(f"Error: {student_file} not found!")
        return
    with open(student_info_file, 'w') as file:
        file.write(",".join(headers) + "\n")
        for student_data in students.values():
            file.write(",".join(student_data) + "\n")
merge_student_data("students.csv", "Student_Info.csv")

def update_info(student):
    with open("Student_Info.csv", 'r') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')
    updated = []
    for line in lines[1:]:
        values = line.strip().split(',')
        if values[0] == student['username']:
            new_values = []
            for header in headers:
                if header in student:
                    new_values.append(str(student[header]))
                else:
                    index = headers.index(header)
                    new_values.append(values[index])
            updated.append(','.join(new_values))
        else:
            updated.append(line.strip())
    with open("Student_Info.csv", 'w') as file:
        file.write(lines[0])
        file.write('\n'.join(updated) + '\n')
    print("Student info updated successfully!")

def get_letter_grade(score):
    try:
        score = float(score)
        if score >= 90: return "A+"
        if score >= 80: return "A"
        if score >= 70: return "B+"
        if score >= 60: return "B"
        if score >= 50: return "C"
        if score >= 40: return "D"
        return "F"
    except ValueError:
        return print("Invalid number")

def get_student_grade(course_name, student_grades):
    grades = {grade['course_name']: grade['final_grade'] for grade in student_grades}
    if course_name in grades:
        score = grades[course_name]
        return f"{score} ({get_letter_grade(score)})"
    return "No grade available."

def login(students):
    while True:
        print("=" * 69)
        user_input = input("Enter username and password (space-separated): ").strip().lower().split()
        if len(user_input) != 2:
            print("Invalid input format")
            continue
        username, password = user_input
        for student in students:
            if student.get('username') == username and student.get('password') == password:
                print("Login successful!")
                return student
        print("Invalid Username or Password")

def student_menu(student, lessons, all_grades, timetable, teachers, events,):
    while True:
        print("=============== Main Menu ===============")
        print("1. Account Management")
        print("2. Course Enrollment")
        print("3. Course Materials")
        print("4. Check Grades")
        print("5. Submit Feedback")
        print("6. View Timetable")
        print("7. Announcements")
        print("8. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            account_management(student)
        elif choice == "2":
            enroll_subject(student, lessons)
        elif choice == "3":
            course_materials(student, lessons)
        elif choice == "4":
            check_grades(student, all_grades)
        elif choice == "5":
            submit_feedback(student, teachers)
        elif choice == "6":
            display_timetable(student, timetable)
        elif choice == "7":
            announcements(student, events)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

def account_management(student):
    while True:
        print("=============== Account Info ===============")
        print(f"Name: {student['name']}")
        print(f"Address: {student['address']}")
        print(f"Phone: {student['phone']}")
        print(f"Email: {student['email']}")
        print(f"Emergency: {student['Emergency']}")
        print(f"Password:  {student['password']}")
        try:
            choice = int(input("Update info? (1-Yes, 0-No): "))
            if choice == 1:
                field_choice = int(input("Which detail do you want to update? (1. Name 2. Address 3. Phone 4. Email 5. Emergency 6. Password) Enter number: "))
                if field_choice == 1:
                    student['name'] = input("Enter new Name: ")
                elif field_choice == 2:
                    student['address'] = input("Enter new Address: ")
                elif field_choice == 3:
                    student['phone'] = input("Enter new Phone: ")
                elif field_choice == 4:
                    student['email'] = input("Enter new Email: ")
                elif field_choice == 5:
                    student['Emergency'] = input("Enter new Emergency Contact: ")
                elif field_choice == 6:
                    student['password'] = input("Enter new Password: ")
                else:
                    print("Invalid choice.")
                    continue
                print("Update successful!")
                update_info(student)
            elif choice == 0:
                break
            else:
                print("Invalid input. Please enter 1 or 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def enroll_subject(student, lessons):
    student_diploma = None
    try:
        with open("student_enrollment.csv", 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        i = 1
        while i < len(lines):
            values = lines[i].split(',')
            if len(values) >= 2 and values[0].strip().lower() == student['name'].strip().lower():
                student_diploma = values[1].strip()
                break
            i += 1
    except FileNotFoundError:
        print("Error: student_enrollment.csv not found!")
        return
    if not student_diploma:
        print("You are not enrolled in any diploma.")
        return
    enrolled_courses = set()
    try:
        with open("enrollment.csv", 'r') as file:
            for line in file:
                values = line.strip().split(',')
                if len(values) == 2 and values[0].strip().lower() == student['username'].strip().lower():
                    enrolled_courses.add(values[1].strip())
    except FileNotFoundError:
        print("Error: enrollment.csv not found!")
        return
    available_courses_for_diploma = []
    for course_name in lessons.keys():
        j = 0
        while j < len(lessons.get(course_name, [])):
            lesson = lessons[course_name][j]
            course_offering = lesson.get("course_offering", "").strip()
            if course_offering and course_offering.title() == student_diploma.title() and course_name not in enrolled_courses:
                available_courses_for_diploma.append(course_name)
                break
            j += 1
    if not available_courses_for_diploma:
        print("No courses available for your diploma or you are already enrolled in all available courses.")
        return
    print("============== Available Courses for " + student_diploma + " ===============")
    i = 0
    while i < len(available_courses_for_diploma):
        print(str(i + 1) + ". " + available_courses_for_diploma[i])
        i += 1
    try:
        choice = input("Select a course to enroll in (0 to cancel): ").strip()
        if choice == "0":
            return
        choice = int(choice) - 1
        if 0 <= choice < len(available_courses_for_diploma):
            selected_course = available_courses_for_diploma[choice]
            with open("enrollment.csv", 'a') as file:
                file.write(student['username'] + "," + selected_course + "\n")
            if 'Courses' in student and student['Courses']:
                student['Courses'] += ";" + selected_course
            else:
                student['Courses'] = selected_course
            print("Enrolled in " + selected_course + " successfully!")
            print("Updated Enrolled Courses:", student['Courses'])
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def course_materials(student, lessons):
    while True:
        courses = student.get('Courses', '').split(';') if student.get('Courses') else []
        if not courses:
            print("No enrolled courses.")
            return
        while True:
            print("=============== Course Materials ===============")
            for i in range(len(courses)):
                print(str(i + 1) + ". " + courses[i])
            try:
                choice = input(f"Select course (1-{len(courses)}, or 0 to cancel): ").strip()
                if choice == "0":
                    return
                choice = int(choice) - 1
                if 0 <= choice < len(courses):
                    selected_course = courses[choice]
                    break
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(courses)}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {len(courses)}.")
        while True:
            course_materials = lessons.get(selected_course, [])
            print(f"=============== Materials for {selected_course} ===============")
            if not course_materials:
                print("No materials available for " + selected_course + ".")
            else:
                for lesson in course_materials:
                    lesson_title = lesson.get('lesson_title', 'No title')
                    lesson_duration = lesson.get('lesson_duration', 'Unknown duration')
                    assignment_name = lesson.get('assignment_name', 'No assignment')
                    assignment_due = lesson.get('assignment_due_date', 'No due date')
                    print(f"- {lesson_title} ({lesson_duration})")
                    print(f"  Assignment: {assignment_name}")
                    print(f"  Due Date  : {assignment_due}")
                    print("---------------------------------------")
            back = input("Press Enter to refresh or 0 to go back to Course Materials: ").strip()
            if back == "":
                continue
            elif back == "0":
                break
            else:
                print("Invalid input. Please enter 0 or press Enter to refresh.")

def check_grades(student, all_grades):
    while True:
        print("=============== Grades ===============")
        student_id = student.get('username', '').strip().lower()
        student_courses = student.get('Courses', '').split(';') if student.get('Courses') else []
        student_grades = {}
        for grade in all_grades:
            if grade.get('student_name', '').strip().lower() == student_id:
                course_name = grade.get('course_name', '').strip()
                student_grades.setdefault(course_name, []).append(grade)
        if not student_courses:
            print("You are not enrolled in any courses.")
        else:
            for course in student_courses:
                course = course.strip()
                if course in student_grades:
                    print(f"{course}")
                    for grade in student_grades[course]:
                        assignment_name = grade.get("assignment_name", "Unknown Assignment").strip()
                        final_grade = grade.get("final_grade", "").strip()
                        if not final_grade:
                            final_grade = "In grading"
                        else:
                            final_grade = f"{final_grade} ({get_letter_grade(final_grade)})"
                        print(f"{assignment_name}: {final_grade}")
                else:
                    print(f"{course} - No grades yet. (In grading)")
        print("="*69)
        back = input("Press Enter to refresh or 0 to go menu: ").strip()
        if back == "":
            continue
        elif back == "0":
            break
        else:
            print("Invalid input. Please enter 0 or press Enter to refresh.")

def submit_feedback(student, teachers):
    while True:
        print("=============== Feedback ===============")
        print("1. Course Feedback")
        print("2. Teacher Feedback")
        print("3. Menu")
        choice = input("Please select an option: ").strip()
        if choice == "1":
            courses = student.get('Courses', '').split(';') if student.get('Courses') else []
            if not courses:
                print("No courses enrolled.")
                return
            for i in range(len(courses)):
                print(f"{i + 1}. {courses[i]}")
            try:
                course_choice = input("Select course (0 to cancel): ").strip()
                if course_choice == "0":
                    return
                course_choice = int(course_choice) - 1
                if 0 <= course_choice < len(courses):
                    selected_course = courses[course_choice]
                    feedback = input("Enter your feedback: ").strip()
                    with open("Student_Feedback.csv", 'a') as file:
                        file.write(f"\n{student['username']},{selected_course},,{feedback},")
                    print("Course feedback submitted!")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            courses = student.get('Courses', '').split(';') if student.get('Courses') else []
            if not courses:
                print("No enrolled courses found.")
                return
            for i in range(len(courses)):
                course_key = courses[i].strip().lower()
                teacher_name = teachers.get(course_key, "Unknown Teacher")
                print(f"{i + 1}. {courses[i]} - {teacher_name}")
            try:
                teacher_choice = input("Select a teacher based on your course (0 to cancel): ").strip()
                if teacher_choice == "0":
                    return
                teacher_choice = int(teacher_choice) - 1
                if 0 <= teacher_choice < len(courses):
                    selected_course = courses[teacher_choice]
                    selected_teacher = teachers.get(selected_course.lower(), "Unknown Teacher")
                    feedback = input(f"Enter your feedback for {selected_teacher}: ").strip()
                    with open("Student_Feedback.csv", 'a') as file:
                        file.write(f"\n{student['username']},{selected_course},{selected_teacher},{feedback}")
                    print("Teacher feedback submitted!")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            return
        else:
            print("Invalid input. Please enter a valid choice.")

def display_timetable(student, timetable):
    try:
        print("=============== Timetable ===============")
        enrolled_courses = [course.strip().lower() for course in student.get('Courses', '').split(';') if course.strip()]

        student_schedule = []
        for entry in timetable:
            timetable_course = entry.get('Course Name', '').strip().lower()

            if timetable_course in enrolled_courses:
                student_schedule.append(entry)
        if not student_schedule:
            print("No schedule available for your enrolled courses.")
            return
        sorted_schedule = []
        for entry in student_schedule:
            week_str = entry.get('Week', '').lower().replace("week", "").strip()
            try:
                week_num = int(week_str)
            except ValueError:
                week_num = 0
            sorted_schedule.append((week_num, entry))
        for i in range(len(sorted_schedule) - 1):
            for j in range(i + 1, len(sorted_schedule)):
                if sorted_schedule[i][0] > sorted_schedule[j][0]:
                    sorted_schedule[i], sorted_schedule[j] = sorted_schedule[j], sorted_schedule[i]
        for week_num, entry in sorted_schedule:
            print(f"Course   : {entry.get('Course Name', 'N/A')}")
            print(f"Week     : {entry.get('Week', 'N/A')}")
            print(f"Date     : {entry.get('Date', 'N/A')}")
            print(f"Time     : {entry.get('Time', 'N/A')}")
            print("=" * 40)
        while True:
            back = input("Press Enter to go menu: ").strip()
            if back ==  "":
                return
            else:
                print("Invalid input. Please enter 0 or press Enter to refresh.")
    except Exception as e:
        print(f"Error displaying timetable: {e}")

def announcements(student, events):
    try:
        student_name = student.get('name', '').strip().lower()
        if student_name not in events or not events[student_name]:
            print("No announcements available for you.")
            return
        print("=============== Announcements ===============")
        for entry in events[student_name]:
            print(f"Event     : {entry.get('event name', 'N/A')}")
            print(f"Date      : {entry.get('date', 'N/A')}")
            print(f"Day       : {entry.get('day', 'N/A')}")
            print(f"Time      : {entry.get('time', 'N/A')}")
            print("=" * 40)
        while True:
            back = input("Press Enter to refresh or 0 to go menu: ").strip()
            if back == "0":
                return
            elif back == "":
                return
            else:
                print("Invalid input. Please enter 0 or press Enter to refresh.")
    except Exception as e:
        print(f"Error displaying announcements: {e}")

def menu_student():
    data = load_data("Student_Info.csv", "enrollment.csv", "Teacher_info.csv", "lesson.csv", "grades.csv", "S-timetable.csv", "event.csv", "available_courses.csv")
    student = login(data["students"])
    student_menu(student, data["lessons"], data["grades"], data["timetable"], data["teachers"], data["events"])

def login_staff():
    staff_users, staff_passwords = read_csv("staff.csv")
    while True:
        username = input("Enter your staff username: ")
        password = input("Enter your password: ")

        if username in staff_users:
            index = staff_users.index(username)
            if staff_passwords[index] == password:
                print("Sign-in successful!")
                staff_menu()
                break
            else:
                print("Incorrect password. Please re-enter.")
        else:
            print("Username not found. Please re-enter.")


def write_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.writelines(f'{data}\n')
    except FileNotFoundError:
        print('\nfile not found')
        return


# Function to read data from a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            if data:
                print(f'\n{data}')
                return
            else:
                print('\nno data found')
                return
    except FileNotFoundError:
        print('\nfile not found')
        return

# Function to merge and view contents of two files
def merge_view(file1, file2):
    for filename in [file1, file2]:
        with open(filename, 'r') as f:
            lines = f.read()
        print('\n' + lines)


# Function to check if user wants to exit (string input)
def str_exit(target):
    if target.lower() == 'exit':
        print('\nExiting')
        return True
    return False


# Function to check if user wants to exit (integer input)
def int_exit(target):
    if target == '0':
        print('\nExiting')
        return True
    return False


# Function to update data in a file
def update_data(filename):
    try:
        read_file(filename)

        with open(filename, 'r') as file:
            lines = file.readlines()

        has_serial_number = False
        for line in lines:
            if line.strip() and line[0] in '0123456789':
                has_serial_number = True
                break

        if has_serial_number:
            serial_number = input('Which line number you want to change? (enter 0 to exit): ')
            if int_exit(serial_number):
                return
            serial_number = int(serial_number)

            if serial_number < 1 or serial_number > len(lines):
                print('\nInvalid serial number')
                return

            target_line = lines[serial_number - 1]
        else:
            target_line = None
            serial_number = None

        print('\nEnter "exit" to go out')
        target_word = input(f'Enter the data you want to change: ')
        if str_exit(target_word):
            return

        if target_line is None:
            for i in range(len(lines)):
                if target_word in lines[i]:
                    target_line = lines[i]
                    serial_number = i + 1
                    break

            if target_line is None:
                print(f'\n"{target_word}" not found in the file')
                return

        if target_word not in target_line:
            print(f'\n"{target_word}" not found in line {serial_number}')
            return

        result = input('Change to what data?: ')
        if str_exit(result):
            return

        new_line = target_line.replace(target_word, result)
        lines[serial_number - 1] = new_line

        with open(filename, 'w') as file:
            file.writelines(lines)

        print(f'\nLine {serial_number} successfully updated.')

    except FileNotFoundError:
        print('\nFile not found')


# Function to delete data from a file
def delete_data(filename):
    try:
        read_file(filename)

        with open(filename, 'r') as file:
            lines = file.readlines()

        has_serial_number = False
        for line in lines:
            if line.strip() and line[0] in '0123456789':
                has_serial_number = True
                break

        if has_serial_number:
            serial_number = input('Which line number you want to delete? (enter 0 to exit): ')
            if int_exit(serial_number):
                return
            serial_number = int(serial_number)

            if serial_number < 1 or serial_number > len(lines):
                print('\nInvalid serial number')
                return

            target_line = lines[serial_number - 1]
        else:

            target_line = None
            serial_number = None

        print('\nEnter "exit" to go out')
        target_word = input(f'Enter the data you want to delete: ')
        if str_exit(target_word):
            return

        if target_line is None:
            for i in range(len(lines)):
                if target_word in lines[i]:
                    target_line = lines[i]
                    serial_number = i + 1
                    break

            if target_line is None:
                print(f'\n"{target_word}" not found in the file')
                return

        if target_word not in target_line:
            print(f'\n"{target_word}" not found in line {serial_number}')
            return

        confirm = input(f'Are you sure you want to delete line {target_word}? (yes/no): ').lower()
        if confirm != 'yes':
            print('\nDeletion canceled')
            return

        deleted_line = lines[serial_number - 1]
        del lines[serial_number - 1]

        if has_serial_number:
            for i in range(len(lines)):
                if lines[i].strip():
                    parts = lines[i].split('.', 1)
                    if len(parts) > 1:
                        lines[i] = f'{i + 1}.{parts[1]}'

        with open(filename, 'w') as file:
            file.writelines(lines)

        print(f'\nLine {serial_number} successfully deleted: {deleted_line.strip()}')

    except FileNotFoundError:
        print('\nFile not found')
        return


# Function to add a new student record
def add_student():
    try:
        student_enrollment = 'student_enrollment.csv'
        available_course = 'available_courses.csv'
        parent_file = 'parent.csv'
        student_name_file = 'Student_Info.csv'

        print('\nenter exit to go out')
        student_name = input('enter your name:').title()
        if str_exit(student_name):
            return

        read_file(available_course)
        course = input('enter your course:')
        if str_exit(course):
            return

        password = input('enter your password:')
        if str_exit(password):
            return

        address = input('enter your state:').title()
        if str_exit(address):
            return

        phone_number = input('enter your phone number(enter 0 to exit):')
        if int_exit(phone_number):
            return
        phone_number = int(phone_number)

        email = input('input your email:')
        if int_exit(email):
            return

        student_id = input('enter your student id:').lower()
        if str_exit(student_id):
            return

        student_father_name = input('enter father name:').title()
        if str_exit(student_father_name):
            return

        father_contact_number = input('enter phone number(enter 0 to exit):')
        if int_exit(father_contact_number):
            return
        father_contact_number = int(father_contact_number)

        student_mother_name = input('enter mother name:').title()
        if str_exit(student_mother_name):
            return

        mother_contact_number = input('enter phone number(enter 0 to exit):')
        if int_exit(mother_contact_number):
            return
        mother_contact_number = int(mother_contact_number)

        emergency = input('enter emergency number(enter 0 to exit):')
        if int_exit(emergency):
            return
        emergency = int(emergency)

        parent_record = f'{student_name}, {student_father_name}, {father_contact_number}, {student_mother_name}, {mother_contact_number}'

        try:
            with open(parent_file, 'x') as file:
                file.writelines('student name, father name, contact number, mother name, contact number\n')
        except FileExistsError:
            pass

        write_file(parent_file, parent_record)

        student_record = f'{student_id},{password},{student_name}, {address}, {phone_number}, {email}, {emergency}'

        try:
            with open(student_name_file, 'x') as file:
                file.writelines('username, password, name, address, phone, email, emergency\n')
        except FileExistsError:
            pass

        write_file(student_name_file, student_record)

        course_record = f'{student_name}, {course}'

        try:
            with open(student_enrollment, 'x') as file:
                file.writelines('name, course\n')
        except FileExistsError:
            pass

        write_file(student_enrollment, course_record)

        print(f'\nsuccessfully added')

    except FileNotFoundError:
        print('\nfile not found')
        return


# Function to update student information
def update_student():
    print('\nwhat you want to change?''\n1. student information''\n2. student course')
    choice = input('enter your choice:')
    if choice == '1':
        student_name_file = 'Student_Info.csv'
        update_data(student_name_file)
    if choice == '2':
        student_enrollment = 'student_enrollment.csv'
        update_data(student_enrollment)
    else:
        print('Invalid')


# Function to handle student transfer processes
def transfer_processes():
    try:
        student_name_file = 'Student_Info.csv'
        transfer_file = 'transfer.csv'

        read_file(student_name_file)
        print('\nenter exit to go out')
        target_name = input('enter name:').title()
        if str_exit(target_name):
            return

        tp_number = input('enter TP number:')
        if int_exit(tp_number):
            return

        reason = input('enter reason:').title()
        if str_exit(reason):
            return

        transfer_school = input('transfer to where:').title()
        if str_exit(transfer_school):
            return

        with open(student_name_file, 'r') as file:
            lines = file.readlines()

        selected_data = [line for line in lines if target_name in line and tp_number in line]
        remaining_data = [line for line in lines if target_name not in line or tp_number not in line]

        if not selected_data:
            print(f'\n{target_name}, {tp_number} not found')
            return

        try:
            with open(transfer_file, 'x') as file:
                file.writelines('username, password, student name, address, contact number, gmail, emergency, reason, transfer to where?\n')
        except FileExistsError:
            pass

        with open(transfer_file, 'a') as file:
            for data in selected_data:
                file.writelines(f'{data.strip()},{reason},{transfer_school}\n')

        with open(student_name_file, 'w') as file:
            file.writelines(remaining_data)

        print(f'\nSuccessfully submitted, please wait for the result')

    except FileNotFoundError:
        print('\nfile not found')
        return


# Function to handle student withdrawal processes
def withdrawal_processes():
    try:
        student_name_file = 'Student_Info.csv'
        withdrawal_file = 'withdrawal.csv'

        read_file(student_name_file)
        print('\nenter exit to go out')
        target_name = input('enter name:').title()
        if str_exit(target_name):
            return

        tp_number = input('enter TP number:')
        if int_exit(tp_number):
            return

        reason = input('enter reason:').title()
        if str_exit(reason):
            return

        with open(student_name_file, 'r') as file:
            lines = file.readlines()

        selected_data = [line for line in lines if target_name in line and tp_number in line]
        remaining_data = [line for line in lines if target_name not in line or tp_number not in line]

        if not selected_data:
            print(f'\n{target_name}, {tp_number} not found')
            return

        try:
            with open(withdrawal_file, 'x') as file:
                file.writelines('username, password, student name, address, contact number, gmail, emergency, transfer to where?\n')
        except FileExistsError:
            pass

        with open(withdrawal_file, 'a') as file:
            for data in selected_data:
                file.writelines(f'{data.strip()},{reason}\n')

        with open(student_name_file, 'w') as file:
            file.writelines(remaining_data)

        print(f'\nSuccessfully submitted, please wait for the result')

    except FileNotFoundError:
        print('\nfile not found')
        return


# Function to manage parent records
def manage_parent():
    while True:
        parent_file = 'parent.csv'
        print('\n1. View parents')
        print('2. Delete parent')
        print('3. Update parent')
        print('4. Back to main menu')
        choice7 = input('Enter your choice:')
        if choice7 == '1':
            read_file(parent_file)
        elif choice7 == '2':
            delete_data(parent_file)
        elif choice7 == '3':
            update_data(parent_file)
        elif choice7 == '4':
            return
        else:
            print('\nInvalid')


# Function to add timetable entries
def add_timetable(filename):
    try:
        lesson_file = 'lesson.csv'

        print('\nEnter "exit" to go out')
        name = input('Enter your name: ').title()
        if str_exit(name):
            return

        id_number = input('Enter your id number: ').lower()
        if str_exit(id_number):
            return

        week = input('Enter week you want (1-12): ')
        if str_exit(week):
            return
        if week not in [str(i) for i in range(1, 13)]:
            print('\nInvalid week number')
            return

        with open(lesson_file, 'r') as file:
            lines = file.readlines()

        print('\nAvailable courses:')
        #Display the data in the first column and duplicates will only be displayed once.
        unique_courses = set()
        for line in lines:
            columns = line.strip().split(",")
            if len(columns) > 0:
                course_name = columns[0].strip()
                unique_courses.add(course_name)

        for course in unique_courses:
            print(course)
        print('Exam')

        course_name = input('\nEnter your choice (course name): ').title()
        if str_exit(course_name):
            return

        else:
            selected_data = [line for line in lines if course_name in line]# check course_name can match with the data or not
            if not selected_data:
                print(f'\nCourse "{course_name}" not found')
                return

        timeslot = input('Enter date(eg: mon):').upper()
        if str_exit(timeslot):
            return

        time = input('enter time(eg: 11:00-12:00):')
        if str_exit(time):
            return

        timetable_record = f'{name}, {id_number}, WEEK{week}, {course_name}, {timeslot}, {time}'

        try:
            with open(filename, 'x') as file:
                file.writelines('name, username, week, course name, date, time\n')
        except FileExistsError:
            pass

        with open(filename, 'a') as file:
            file.writelines(timetable_record + '\n')

        print(f'\nSuccessfully added!')
        return

    except FileNotFoundError:
        print('\nFile not found')
        return


# Function to add resource allocations
def add_resources():
    while True:
        resources_file = 'resources.csv'

        print('\nWho are you?\n1. Student\n2. Teacher\n3. Back to main menu')
        choice14 = input('Enter your choice:')
        if choice14 == "1":
            who = 'Student'
        elif choice14 == '2':
            who = 'Teacher'
        elif choice14 == '3':
            return
        else:
            print('\nInvalid')
            return

        print('\nEnter exit to go out')
        print('1. Projectors \n2. Computers \n3. Books')
        choice13 = input('Enter your choice:')
        if choice13.lower() == 'exit':
            print('\nExiting...')
            return
        if choice13 == '1':
            resource_name = 'Projectors'
        elif choice13 == '2':
            resource_name = 'Computers'
        elif choice13 == '3':
            resource_name = 'Books'
        else:
            print('\nInvalid')
            return

        resources_studentname = input('Enter your name:').title()
        if resources_studentname.lower() == 'exit':
            print('\nExiting')
            return
        resources_studentid = input('Enter your id:').lower()
        if resources_studentid.lower() == 'exit':
            print('\nExiting')
            return
        resources_class = input('Enter the class where you borrow the item:')
        if resources_class.lower() == 'exit':
            print('\nExiting')
            return

        resource_timeslot = input('Enter date(eg: mon date/time/year 11:00-12:00)').upper()
        if resource_timeslot.lower() == 'exit':
            print('\nExiting')
            return

        resource_record = f'{resources_studentname}, {who}, {resources_studentid}, {resource_name}, {resource_timeslot}, {resources_class}'

        try:
            with open(resources_file, 'x') as file:
                file.writelines('name, student/teacher, id, resource name, day, date, time, class\n')
        except FileExistsError:
            pass

        write_file(resources_file, resource_record)

        print(f'{resource_name} successfully added!')
        break


# Function to add events
def add_event():
    event_file  = 'event.csv'

    print('\nEnter exit to go out')
    print('\n1. holiday\n2. Semester Break\n3.Extracurricular events\n4. Conferences\n5. Seminars')
    choice15 = input('Enter your choice:')
    if str_exit(choice15):
        return
    elif choice15 == '1':
        event_name = 'Holiday'
    elif choice15 == '2':
        event_name = 'Semester Break'
    elif choice15 == '3':
        event_name = input("Please enter the event name:").title()
        if str_exit(event_name):
            return
    elif choice15 == '4':
        event_name = 'conferences'
    elif choice15 == '5':
        event_name = 'seminars'
    else:
        print('\nInvalid')
        return

    student_name = input('please enter your name:').title()
    if str_exit(student_name):
        return

    event_day = input('enter the day(eg: mon):').upper()
    if str_exit(event_day):
        return

    event_date = input("Please enter the date(eg: date/month/year):")
    if str_exit(event_date):
        return

    event_time = input("Please enter the time(eg:15.30-17.30):")
    if str_exit(event_time):
        return

    try:
        with open(event_file, 'r') as file:
            lines = file.readlines()[1:]
            count = len(lines) + 1
    except FileNotFoundError:
        count = 1

    event_record = f'{count}, {event_name}, {student_name}, {event_day}, {event_date}, {event_time}'

    try:
        with open(event_file, 'x') as file:
            file.writelines('serial number, event name, username, day, date, time\n')
    except FileExistsError:
        pass

    write_file(event_file, event_record)

    print(f"\n{event_name} successfully added!")


# Function to add teacher records
def add_teacher():
    teacher_file = 'teacher_information.csv'
    print('\nEnter exit to go out')
    teacher_name = input('Enter your name:').title()
    if str_exit(teacher_name):
        return
    teacher_id = input('Enter your id:').lower()
    if str_exit(teacher_id):
        return
    teacher_gmail = input('Enter your email:')
    if str_exit(teacher_gmail):
        return

    teacher_record = f'{teacher_name}, {teacher_id}, {teacher_gmail}'

    try:
        with open(teacher_file, 'x') as file:
            file.writelines('teacher name, teacher id, teacher gmail\n')
    except FileExistsError:
        pass

    write_file(teacher_file, teacher_record)
    print(f'\n{teacher_name} successfully added.')


# Main staff menu function
def staff_menu():
    while True:
        print("\nSCHOOL MANAGEMENT SYSTEM")
        print("1. Manage Student Records")
        print("2. Manage Timetables")
        print("3. Allocate Resources")
        print("4. Manage Events")
        print("5. Teacher Record")
        print("6. Exit")
        choice = input("Enter your choice(1-6):")

        # Student management section
        if choice == "1":
            while True:
                student_name_file  = 'Student_Info.csv'
                student_enrollment = 'student_enrollment.csv'
                print("\nSTUDENT RECORD")
                print("1. Add Student")
                print("2. View Student")
                print('3. Update student')
                print("4. Transfer processes")
                print('5. Withdrawal processes')
                print('6. Parent record')
                print("7. Back To Main Menu")
                choice2 = input("Enter your choice(1-7):")
                if choice2 == "1":
                    add_student()
                elif choice2 == "2":
                    merge_view(student_name_file, student_enrollment)
                elif choice2 == "3":
                    update_student()
                elif choice2 == "4":
                    transfer_processes()
                elif choice2 == '5':
                    withdrawal_processes()
                elif choice2 == '6':
                    manage_parent()
                elif choice2 == "7":
                    break
                else:
                    print("\nInvalid")

        # Timetable management section
        elif choice == "2":
            while True:
                timetable = 'S-timetable.csv'
                print("\nTIMETABLE MANAGEMENT")
                print('1. Add timetable')
                print('2. Delete timetable')
                print('3. View timetable')
                print('4. Update timetable')
                print('5. Back to main menu')
                choice3 = input('Enter your choice(1-5):')
                if choice3 == '1':
                    add_timetable(timetable)
                if choice3 == '2':
                    delete_data(timetable)
                if choice3 == '3':
                    read_file(timetable)
                if choice3 == '4':
                    update_data(timetable)
                elif choice3 == '5':
                    break
                else:
                    print('\nInvalid')

        # Resource management section
        elif choice == "3":
            while True:
                resources_file = 'resources.csv'
                print("\nResources management")
                print('1. Add resources')
                print('2. Delete resources')
                print('3. View resources')
                print('4. Update resources')
                print('5. Back to main menu')
                choice4 = input('Enter your choice(1-5):')
                if choice4 == '1':
                    add_resources()
                if choice4 == '2':
                    delete_data(resources_file)
                if choice4 == '3':
                    read_file(resources_file)
                if choice4 == '4':
                    update_data(resources_file)
                elif choice4 == '5':
                    break
                else:
                    print('\nInvalid')

        # Event management section
        elif choice == "4":
            while True:
                event_file = 'event.csv'
                print("\nEVENT MANAGEMENT")
                print("1. Add event")
                print("2. Delete event")
                print("3. View event")
                print('4. Update event')
                print("5. Back to main menu")
                choice5 = input("Enter your choice(1-5):")
                if choice5 == "1":
                    add_event()
                if choice5 == "2":
                    delete_data(event_file)
                if choice5 == "3":
                    read_file(event_file)
                if choice5 == '4':
                    update_data(event_file)
                if choice5 == "5":
                    break
                else:
                    print("\nInvalid")

        # Teacher management section
        elif choice == "5":
            while True:
                teacher_file = 'teacher_information.csv'
                print('\n TEACHER RECORD')
                print("1. Add teacher")
                print("2. Delete teacher")
                print("3. View teacher")
                print('4. Update teacher')
                print('5. Back to main menu')
                choice6 = input('Enter your choice(1-5):')
                if choice6 == '1':
                    add_teacher()
                if choice6 == '2':
                    delete_data(teacher_file)
                if choice6 == '3':
                    read_file(teacher_file)
                if choice6 == '4':
                    update_data(teacher_file)
                if choice6 == '5':
                    break
                else:
                    print('\nInvalid')

        elif choice == "6":
            break

        else:
            print('\nInvalid')

def teacher_portal():
    teacher_name = input("\nEnter your name: ").strip()
    password_t = input("Enter your password: ").strip()
    with open('teachers.csv', 'r') as teacher_file:
        teacher_details = teacher_file.readlines()
    for line in teacher_details:
        stored_name, stored_password = line.strip().split(',')
        if teacher_name == stored_name and password_t == stored_password:
            print(f"Welcome, {teacher_name}")
            menu_teacher(teacher_name, password_t)
            return teacher_name , password_t
    print("Invalid credentials. Please try again.")
    return None

def course_menu(teacher_name):
    while True:
        print("\nSelect an option:")
        print("1. Create Course")
        print("2. Update Course")
        print("3. View Courses")
        print("4. Exit")
        try:
            choice = int(input("Enter (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            create_course(teacher_name)
        elif choice == 2:
            update_course(teacher_name)
        elif choice == 3:
            view_course(teacher_name)
        elif choice == 4:
            print("Exiting Course Menu.")
            break
        else:
            print("Invalid option. Please enter a number (1-4).")

def create_course(teacher_name):
    course_name = input("Enter course name: ").strip()
    lesson_number = input("Enter lesson number: ").strip()
    lesson_title = input("Enter lesson title: ").strip()
    lesson_duration = input("Enter lesson duration (in hours): ").strip()
    assignment_name = input("Enter assignment name: ").strip()
    assignment_due_date = input("Enter assignment due date (YYYY-MM-DD): ").strip()
    course_offering = input("Enter course offering term: ").strip()
    with open("lesson.csv", "a") as lesson:
        lesson.write(f"{course_name},{lesson_number},{lesson_title},{lesson_duration},{assignment_name},{assignment_due_date},{teacher_name},{course_offering}\n")
    with open("teacher_info.csv",'a') as teacher_assign:
        teacher_assign.write(f"{teacher_name},{course_name}")
    print("Course added successfully!")

def update_course(teacher_name):
    # Load courses from file
    with open("lesson.csv", "r") as file:
        courses = file.readlines()
    # Filter courses that belong to the teacher
    teacher_courses = []
    for course in courses:
        course_details = course.strip().split(',')
        if course_details[6] == teacher_name:
            teacher_courses.append(course)
    if not teacher_courses:
        print("No courses found under your name.")
        return
    # Display teacher's courses
    print("\nYour Courses:")
    for i, course in enumerate(teacher_courses, start=1):
        data = course.strip().split(',')
        print(f"{i}. {data[0]} - {data[2]} (Lesson {data[1]})")
    try:
        choice = int(input("\nSelect a course to update (Enter number): ")) - 1
        if choice < 0 or choice >= len(teacher_courses):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    # Split selected course data
    selected_course = teacher_courses[choice].strip().split(',')
    # Get new values (press Enter to keep old values)
    print("\nEnter new details (press Enter to keep the current value):")
    new_lesson_title = input(f"Lesson Title [{selected_course[2]}]: ").strip() or selected_course[2]
    new_lesson_duration = input(f"Lesson Duration [{selected_course[3]} hours]: ").strip() or selected_course[3]
    new_assignment_name = input(f"Assignment Name [{selected_course[4]}]: ").strip() or selected_course[4]
    new_assignment_due_date = input(f"Assignment Due Date [{selected_course[5]}]: ").strip() or selected_course[5]
    new_course_offering = input(f"Course Offering [{selected_course[7]}]: ").strip() or selected_course[7]
    # Update the course
    selected_course[2] = new_lesson_title
    selected_course[3] = new_lesson_duration
    selected_course[4] = new_assignment_name
    selected_course[5] = new_assignment_due_date
    selected_course[7] = new_course_offering
    # Replace old course data in the list
    courses[courses.index(teacher_courses[choice])] = ",".join(selected_course) + "\n"
    # Save updated courses back to file
    with open("lesson.csv", "w") as file:
        file.writelines(courses)
    print("Course updated successfully!")

def view_course(teacher_name):
    try:
        with open('lesson.csv', 'r') as file:
            courses = file.readlines()
        print("\n========== Your Assigned Courses ==========")
        found = False
        for course in courses:
            course_details = course.strip().split(',')
            if len(course_details) < 8:
                continue  # Skip incomplete records
            course_teacher = course_details[6]  # The teacher's name from the CSV
            if course_teacher == teacher_name:
                found = True
                print(f"\nCourse Name: {course_details[0]}")
                print(f"Lesson Number: {course_details[1]}")
                print(f"Lesson Title: {course_details[2]}")
                print(f"Lesson Duration: {course_details[3]}")
                print(f"Assignment Name: {course_details[4]}")
                print(f"Assignment Due Date: {course_details[5]}")
                print(f"Teacher: {course_details[6]}")
                print(f"Course Offering: {course_details[7]}")
                print("-" * 40)
        if not found:
            print("No courses found for you.")
    except FileNotFoundError:
        print("Course file not found. Please ensure 'course.csv' exists.")

def update_schedule(teacher_name, password_t):
    # Read the existing schedule file
    try:
        with open("S-timetable.csv", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    # Read lessons file to get courses for the teacher
    try:
        with open("lesson.csv", "r") as lesson:
            lesson_lines = lesson.readlines()
    except FileNotFoundError:
        print("Error: lesson.csv file not found.")
        return
    # Get courses for the teacher
    courses = []
    for line in lesson_lines[1:]:  # Skip header
        values = line.strip().split(",")
        if len(values) >= 8 and values[6] == teacher_name:
            courses.append(values[0])  # Course Name
    if not courses:
        print("\nNo courses found for you.")
        return
    # Show available courses
    print("\nYour Courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course}")
    try:
        choice = int(input("\nEnter the number of the course (or 0 to cancel): "))
        if choice == 0:
            return
        course_name = courses[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    # Get week number
    week_number = input("\nEnter the week number (1-12): ").strip()
    if not week_number.isdigit() or not (1 <= int(week_number) <= 12):
        print("Invalid week number.")
        return
    # Get schedule details
    date = input("Enter the day (MON, TUE, WED, etc.): ").strip().upper()
    time_slot = input("Enter the time (HHMM-HHMM format): ").strip()
    lesson_name = input("Enter the lesson name: ").strip()
    # Prepare new schedule entry
    new_entry = f"{teacher_name},{password_t},WEEK{week_number},{course_name},{date},{time_slot}\n"
    # Keep old data, but remove existing entry if it has the same teacher, course, week, day, and time
    updated_schedule = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) >= 6:
            existing_teacher, existing_week, existing_course, existing_date, existing_time = (
                parts[0], parts[2], parts[3], parts[4], parts[5]
            )
            if (existing_teacher == teacher_name and existing_week == f"WEEK{week_number}" and
                    existing_course == course_name and existing_date == date and existing_time == time_slot):
                continue  # Skip (remove) the old entry
        updated_schedule.append(line)  # Keep other lines
    # Add new entry
    updated_schedule.append(new_entry)
    # Save updated schedule
    with open("S-timetable.csv", "w") as file:
        file.writelines(updated_schedule)
    print("\nSchedule updated successfully!")

def view_schedule(teacher_name, password_t):
    teacher_courses = set()  # Store courses assigned to the teacher
    try:
        with open("lesson.csv", "r") as file:
            next(file)  # Skip the header row
            for line in file:
                data = line.strip().split(",")  # Split line into a list
                if len(data) > 6 and data[6].strip() == teacher_name:  # Check if teacher matches
                    teacher_courses.add(data[0].strip())  # Store course name
    except FileNotFoundError:
        print("The lesson file is missing.")
        return
    teacher_schedules = []
    try:
        with open("S-timetable.csv", "r") as file:
            next(file)  # Skip the header
            for line in file:
                schedule = line.strip().split(",")
                if schedule[0] == teacher_name and schedule[1] == password_t:  # Check if teacher matches ID
                    teacher_schedules.append(schedule)
    except FileNotFoundError:
        print("The schedule file is missing.")
        return
    if not teacher_schedules:
        print(f"\nNo schedules available for {teacher_name}.")
        return
    print(f"\n=== Schedule for {teacher_name} ===")
    for schedule in teacher_schedules:
        name, username, week, course_name, date, time = schedule
        print(f"\n{course_name} - {week} - {date} at {time}")
        print("=" * 40)

def schedule_menu(teacher_name,password_t):
    while True:
        print("\nChoose a subject")
        print("1. Update Schedule")
        print("2. View Schedule ")
        print("3. Exit")
        try:
            choice_2 = int(input("Enter (1-3): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice_2 == 3:
            print("Exiting Menu")
            break
        elif choice_2 == 1:
            update_schedule(teacher_name,password_t)
        elif choice_2 == 2:
            view_schedule(teacher_name,password_t)
        else:
            print("Invalid option. Please enter (1-3).")
            continue

def enrollment_menu(teacher_name):
    while True:
        print("\n=== Student Enrollment Menu ===")
        print("1. Enroll Student")
        print("2. Remove Student")
        print("3. View Enrolled Students")
        print("4. Exit")
        choice = input("Enter (1-4): ")
        if choice == "1":
            enroll_student(teacher_name)
        elif choice == "2":
            remove_student(teacher_name)
        elif choice == "3":
            view_enrollments(teacher_name)
        elif choice == "4":
            print("Exiting Enrollment Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

def enroll_student(teacher_name):
    students = {}  # Dictionary to store student ID and name
    try:
        with open("Student_Info.csv", "r") as student_details:
            for line in student_details:
                student_info = line.strip().split(",")
                student_id = student_info[0]
                student_name = student_info[2]
                students[student_id] = student_name
    except FileNotFoundError:
        print("Error: file not found.")
        return
    print("\n=== Available Students ===")
    for student_id, student_name in students.items():
        print(f"{student_id} - {student_name}")
    id_number = input("\nEnter the student ID or 'c' to cancel: ").strip()
    if id_number.lower() == 'c':
        print("Cancelled")
        return
    if id_number not in students:
        print("Error: Student ID not found.")
        return
    print(f"Selected Student: {students[id_number]}")
    view_course(teacher_name)
    course_name = input("Enter course name to enroll: ").strip()
    courses = []  # List to store course names
    try:
        with open("lesson.csv", "r") as course_info:
            next(course_info)
            for line in course_info:
                course_title = line.split(",")[0]
                courses.append(course_title)
    except FileNotFoundError:
        print("Error: file not found.")
        return
    if course_name not in courses:
        print(f"Error: Course '{course_name}' does not exist.")
        return
    try:
        with open("enrollment.csv", "a") as file:
            file.write(f"{id_number},{course_name}\n")  # Save only student ID and course
    except Exception as e:
        print(f"Error saving enrollment: {e}")
        return
    print(f"Student ({id_number}) has been enrolled in '{course_name}' successfully!")

def remove_student(teacher_name):
    students = {}
    try:
        with open("Student_Info.csv", "r") as student_details:
            for line in student_details:
                student_info = line.strip().split(",")  # Remove whitespace and split
                student_id = student_info[0]  # First column is the ID
                student_name = student_info[2]  # Third column is the name
                students[student_id] = student_name  # Store ID and Name in dictionary
    except FileNotFoundError:
        print("Error: file not found.")
        return
    print("\n=== Available Students ===")
    for student_id, student_name in students.items():
        print(f"{student_id} - {student_name}")
    id_number = input("\nEnter ID Number to remove or 'c' to cancel: ").strip()
    if id_number.lower() == 'c':
        print("Cancelled")
        return
    if id_number not in students:
        print("Error: Student ID not found.")
        return
    print(f"Selected Student: {students[id_number]}")
    view_course(teacher_name)
    course_name = input("Enter course name to remove student from: ").strip()
    try:
        with open("enrollment.csv", "r") as file:
            enrollments = file.readlines()
    except FileNotFoundError:
        print("No enrollment records found.")
        return
    updated_enrollments = []
    for line in enrollments:
        if line.strip() == f"{id_number},{course_name}":
            # If the line matches the student's enrollment, skip it (remove it)
            continue
        updated_enrollments.append(line)
    if len(updated_enrollments) == len(enrollments):
        print(f"Student ({id_number}) is not enrolled in '{course_name}'.")
        return
    try:
        with open("enrollment.csv", "w") as file:
            file.writelines(updated_enrollments)
    except Exception as e:
        print(f"Error updating enrollment file: {e}")
        return
    print(f"Student ({id_number}) has been removed from '{course_name}' successfully!")


def view_enrollments(teacher_name):
    try:
        # Get the courses where the teacher is assigned to lessons
        teacher_courses = set()
        with open("lesson.csv", "r") as lesson_file:
            for line in lesson_file.readlines()[1:]:  # Skip header
                course_name,lesson_number,lesson_title,lesson_duration,assignment_name,assignment_due_date,teacher,course_offering = line.strip().split(",")
                if teacher == teacher_name:
                    teacher_courses.add(course_name)
        if not teacher_courses:
            print("You are not assigned to any courses.")
            return
        # Read enrollment data and filter by teacher's courses
        with open("enrollment.csv", "r") as enroll_file:
            lines = enroll_file.readlines()
            if len(lines) <= 1:
                print("No students enrolled.")
                return
            print("\n=== Enrolled Students in Your Courses ===")
            found = False
            for line in lines[1:]:
                id_number, course_name = line.strip().split(",")
                if course_name in teacher_courses:
                    print(f"Student: {id_number} | Course: {course_name}")
                    found = True
            if not found:
                print("No students enrolled in your assigned courses.")
            print("=" * 25)
    except FileNotFoundError:
        print("No enrollment records found.")

def grade_student(teacher_name):
    view_enrollments(teacher_name)  # Show enrolled students
    id_number = input("\nEnter ID Number to grade or 'c' to cancel: ").strip()
    if id_number.lower() == 'c':
        print("Cancelled")
        return
    student_name = None
    try:
        with open("Student_Info.csv", "r") as student_file:
            for line in student_file:
                student_data = line.strip().split(",")
                if student_data[0] == id_number:  # Match student ID
                    student_name = student_data[2]  # Get student name
                    break
    except FileNotFoundError:
        print("Error: file not found.")
        return
    if not student_name:
        print("Error: Student ID not found.")
        return
    student_course = None
    try:
        with open("enrollment.csv", "r") as enroll_file:
            next(enroll_file)  # Skip header
            for line in enroll_file:
                data = line.strip().split(",")
                if data[0] == id_number:
                    student_course = data[1]  # Get course name
                    break
    except FileNotFoundError:
        print("Error: file not found.")
        return
    if not student_course:
        print(f"{id_number} is not enrolled in any course.")
        return
    lessons = []
    try:
        with open("lesson.csv", "r") as lesson_details:
            next(lesson_details)  # Skip header
            for line in lesson_details:
                data = line.strip().split(",")
                if data[0] == student_course:
                    lessons.append(data)  # Collect lessons for the course
    except FileNotFoundError:
        print("Error: file not found.")
        return
    if not lessons:
        print(f"No lessons found for {student_course}.")
        return
    print(f"\n=== Lessons for {student_course} ===")
    for i, lesson in enumerate(lessons, start=1):
        print(f"{i}. {lesson[2]} (Assignment: {lesson[4]})")
    try:
        choice = int(input("\nEnter lesson number to grade: ").strip())
        selected_lesson = lessons[choice - 1]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return
    lesson_title, assignment_name = selected_lesson[2], selected_lesson[4]
    try:
        assignment_grade = float(input(f"Enter assignment grade for '{lesson_title}': ").strip())
        exam_grade = float(input(f"Enter exam grade for '{lesson_title}': ").strip())
    except ValueError:
        print("Invalid grade input.")
        return
    final_grade = (assignment_grade + exam_grade) / 2
    # New Inputs: Teacher's Comment & Teacher Name
    teacher_comment = input("Enter teacher's comment on student's performance: ").strip()
    graded_by = input("Enter your name (Grading Teacher): ").strip()
    # Read existing grades
    try:
        with open("report.csv", "r") as grade:
            lines = grade.readlines()
    except FileNotFoundError:
        lines = ["student_name,course_name,lesson_title,assignment_name,assignment_grade,exam_grade,final_grade,teacher_comment,graded_by\n"]
    # Remove old grade entry if it exists
    updated_grade = []
    for line in lines:
        if not line.startswith(f"{student_name},{student_course},{lesson_title},"):
            updated_grade.append(line)  # Keep the line if it doesn’t match the existing record
    updated_grade.append(f"{student_name},{student_course},{lesson_title},{assignment_name},{assignment_grade},{exam_grade},{final_grade:.2f},{teacher_comment},{graded_by}\n")
    with open("report.csv", "w") as grade:
        grade.writelines(updated_grade)
    print(f"Grades recorded: {student_name} ({id_number}) - {lesson_title} (Final: {final_grade:.2f})")
    print(f"Comment: {teacher_comment}")
    print(f"Graded by: {graded_by}")

def mark_attendance(teacher_name):
    view_enrollments(teacher_name)  # Display enrolled students
    student_id = input("\nEnter ID Number to mark attendance or 'c' to cancel: ").strip()
    if student_id.lower() == 'c':
        print("Cancelled.")
        return
    student_name, student_course = None, None
    try:
        with open("enrollment.csv", "r") as file:
            for line in file.readlines()[1:]:  # Skip header
                id_student, course = line.strip().split(",")
                if id_student == student_id:
                    student_course = course
                    break
    except FileNotFoundError:
        print("Error: enrollment.csv not found.")
        return
    if not student_course:
        print("Error: Student is not enrolled in any course.")
        return
    try:
        with open("Student_Info.csv", "r") as file:
            for line in file.readlines()[1:]:  # Skip header
                data = line.strip().split(",")
                if data[0] == student_id:
                    student_name = data[2]  # Get student name
                    break
    except FileNotFoundError:
        print("Error: Student_Info.csv not found.")
        return
    if not student_name:
        print("Error: Student name not found.")
        return
    # Get teacher's assigned lessons
    teacher_lessons = []
    try:
        with open("lesson.csv", "r") as file:
            for line in file.readlines()[1:]:  # Skip header
                data = line.strip().split(",")
                if len(data) < 8:
                    continue  # Skip malformed lines
                course_name, _, lesson_title, _, _, _, teacher, _ = data
                if teacher == teacher_name and course_name == student_course:
                    teacher_lessons.append(lesson_title)
    except FileNotFoundError:
        print("Error: lesson.csv not found.")
        return
    if not teacher_lessons:
        print("Error: You are not assigned to any lessons in this course.")
        return
    # Show lessons
    print(f"\n=== Your Lessons in {student_course} ===")
    for i, lesson in enumerate(teacher_lessons, start=1):
        print(f"{i}. {lesson}")
    try:
        choice = int(input("\nEnter lesson number to mark attendance: ").strip())
        selected_lesson = teacher_lessons[choice - 1]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return
    week_choice = input("Enter the week number: ").strip()
    day_choice = input("Enter the day (e.g., Monday): ").strip().capitalize()
    status = input(f"Mark attendance for {student_name} ({student_id}) in '{selected_lesson}' (Present/Absent): ").strip().capitalize()
    if status not in ["Present", "Absent"]:
        print("Invalid input. Enter 'Present' or 'Absent'.")
        return
    try:
        with open("attendance.csv", "a") as file:
            file.write(f"{student_name},{student_course},{week_choice},{day_choice},{selected_lesson},{status}\n")
        print(f"Attendance recorded: {student_name} ({student_id}) - {selected_lesson} (Week {week_choice}, {day_choice}, [{status}])")
    except Exception as e:
        print(f"Error saving attendance:{e}")

def view_feedback():
    try:
        with open('Student_Feedback.csv', 'r') as file:
            lines = file.readlines()
        if len(lines) <= 1:
            print("No feedback available.")
            return
        print("\nFeedback List:")
        for i, line in enumerate(lines[1:], 1):  # Skip header
            data = line.strip().split(",")
            username = data[0] if len(data) > 0 else "N/A"
            course = data[1] if len(data) > 1 else "N/A"
            lecturer = data[2] if len(data) > 2 else "N/A"
            feedback = data[3] if len(data) > 3 else "No feedback"
            print("=" * 36)
            print(f"{i}. {username} | {course} | {lecturer} | {feedback}")
    except FileNotFoundError:
        print("Feedback file not found.")

def first_menu(teacher_name,password_t):
    while True:
        print("\nChoose a subject")
        print("1. Course")
        print("2. Schedule")
        print("3. Exit")
        try:
            choice_1 = int(input("\nEnter (1-4): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice_1 == 3:
            print("EXIT")
            return
        elif choice_1 == 1:
            course_menu(teacher_name)
        elif choice_1 == 2:
            schedule_menu(teacher_name,password_t)
        else:
            print("Invalid number")
            continue

def second_menu(teacher_name):
    while True:
        print("\nChoose a subject")
        print("1. Student enrollment")
        print("2. Student grading")
        print("3. Student Attendance")
        print("4. Student Feedback")
        print("5. Exit")
        try:
            choice_2 = int(input("Enter (1-5): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice_2 == 5:
            print("Exiting...")
            break
        elif choice_2 == 1:
            enrollment_menu(teacher_name)
        elif choice_2 == 2:
            grade_student(teacher_name)
        elif choice_2 == 3:
            mark_attendance(teacher_name)
        elif choice_2 == 4:
            view_feedback()
        else:
            print("Invalid option. Please enter (1-5).")

def menu_teacher(teacher_name,password_t):
    while True:
        print("\n========== Teacher Menu ==========")
        print("1. Course Management")
        print("2. Student Management")
        print("3. Exit")
        try:
            choice = int(input("Enter (1-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 3:
            print("Exiting...")
            break
        elif choice == 1:
            first_menu(teacher_name,password_t)
        elif choice == 2:
            second_menu(teacher_name)
        else:
            print("Invalid option. Please enter (1-3).")


main_main_menu()



