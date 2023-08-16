class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches or students:
            if sandwiches[0] in students:
                want = students.pop(0)
                if want == sandwiches[0]:
                    sandwiches.pop(0)
                else:
                    students.append(want)
            else:
                break

        return len(students)