class Student:
    # Class variable to track the total number of students
    total_students = 0

    def __init__(self, name, email, student_id, course, marks):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks  # List of numerical marks
        
        # Increment total students whenever a new student is created
        Student.total_students += 1

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")
        print("-" * 30)

    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated for {self.name}.\n")

    def calculate_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    @classmethod
    def get_total_students(cls):
        return cls.total_students

# Example usage
if __name__ == "__main__":
    # Creating multiple student objects
    s1 = Student("Alice Smith", "alice@example.com", "S001", "Computer Science", [85, 90, 88])
    s2 = Student("Bob Johnson", "bob@example.com", "S002", "Mathematics", [78, 82, 80])
    s3 = Student("Charlie Brown", "charlie@example.com", "S003", "Physics", [92, 95, 91])

    print("Initial Student Details:")
    print("=" * 30)
    s1.display_details()
    s2.display_details()
    s3.display_details()
    
    # Updating marks for a student
    s2.update_marks([85, 88, 86])
    
    print("Details after updating marks:")
    print("=" * 30)
    s2.display_details()

    # Using class method to display total students
    print(f"Total Number of Students: {Student.get_total_students()}")
