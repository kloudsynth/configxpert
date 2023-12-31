class UsernamesWithAdmin:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        admin_usernames = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "username" in line.lower() and "admin" in line.lower():
                username = line.split()[1]
                admin_usernames.append(f"{username} on Line {line_number}")

        if admin_usernames:
            comment = ", ".join(admin_usernames)
            return {"value": "FAIL", "comment": comment}
        else:
            return {"value": "PASS", "comment": ""}