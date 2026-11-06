class JobDescription:
    def __init__(self, job_id, company, role, location="Remote", is_active=True):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.job_id} | {self.company} | {self.role} | {self.location} | {status}"

job_one = JobDescription(job_id=101, company="TCS", role="Python Developer")
job_two = JobDescription(job_id=102, company="Infosys", role="Java Developer", location="Pune")
job_three = JobDescription(job_id=103, company="Wipro", role="Tester", location="Nagpur", is_active=False)

jobs = [job_one, job_two, job_three]

for job in jobs:
    print(job)
