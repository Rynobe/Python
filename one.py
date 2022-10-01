#one.py

def func():
    print("FUNC() IN ONE.PY")

def func2():
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    # Run the script!
    func2()
    print("ONE.PY is being run directly!")
else:
    print("ONE.PY has been imported!")
