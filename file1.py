
import file2
print(f"File one __name__ is set to:{__name__}")

if __name__ == "__main__":
    print("File 1 is executed directly")
else:
    print("File 1 is executed when imported")
