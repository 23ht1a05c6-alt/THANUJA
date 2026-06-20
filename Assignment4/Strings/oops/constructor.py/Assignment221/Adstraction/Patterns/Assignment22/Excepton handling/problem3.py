class FileAnalyzer:

    def analyze(self, filename):
        try:
            with open(filename, "r") as file:
                data = file.read()

            words = len(data.split())
            characters = len(data)

            print("File Analysis Report")
            print("Number of Words:", words)
            print("Number of Characters:", characters)

        except FileNotFoundError:
            print("Error: File not found")

        except PermissionError:
            print("Error: Permission denied")

        except Exception as e:
            print("Error:", e)


filename = input("Enter file name: ")

obj = FileAnalyzer()
obj.analyze(filename)


