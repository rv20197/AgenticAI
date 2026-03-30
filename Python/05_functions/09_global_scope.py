chai_type = "Plain Tea"

def front_desk():
    def kitchen():
        global chai_type # Looks into global function
        chai_type = "Irani Tea"
    kitchen()

front_desk()
print(f"Final global tea {chai_type}")