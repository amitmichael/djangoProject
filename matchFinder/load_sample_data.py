from matchFinder.models import *


def load_sample():
    skills = [{"id": 1, "skill_text": "Java"}, {"id": 2, "skill_text": "AWS"}, {"id": 3, "skill_text": "C++"}, {"id": 4, "skill_text": "Git"}, {"id": 5, "skill_text": "Python"}, {"id": 6, "skill_text": "Django"}, {"id": 7, "skill_text": "SQL"}]
    candidates = [{"id": 1, "title": "Software Developer", "name": "Dana"}, {"id": 2, "title": "QA engineer", "name": "Yuval"}, {"id": 3, "title": "QA engineer", "name": "Ron"}, {"id": 4, "title": "Software Developer", "name": "Amit"}, {"id": 5, "title": "Team Leader", "name": "Ido"}, {"id": 6, "title": "Team Leader", "name": "Eden"}, {"id": 7, "title": "R&D manager", "name": "joe"}]
    jobs = [{"id": 1, "title": "Software Developer"}, {"id": 2, "title": "QA engineer"}, {"id": 3, "title": "Team Leader"}, {"id": 4, "title": "Data Analyst"}, {"id": 5, "title": "R&D manager"}, {"id": 6, "title": "Team Leader"}]
    job_requirements = [{"id": 1, "job_id_id": 1, "skill_title_id": 1}, {"id": 2, "job_id_id": 1, "skill_title_id": 3}, {"id": 3, "job_id_id": 2, "skill_title_id": 2}, {"id": 4, "job_id_id": 4, "skill_title_id": 4}, {"id": 5, "job_id_id": 1, "skill_title_id": 5}, {"id": 6, "job_id_id": 1, "skill_title_id": 6}, {"id": 7, "job_id_id": 5, "skill_title_id": 1}, {"id": 8, "job_id_id": 3, "skill_title_id": 4}, {"id": 9, "job_id_id": 3, "skill_title_id": 5}, {"id": 10, "job_id_id": 6, "skill_title_id": 6}, {"id": 11, "job_id_id": 4, "skill_title_id": 7}]
    candidate_abilities = [{"id": 1, "candidate_id_id": 1, "skill_title_id": 1}, {"id": 2, "candidate_id_id": 2, "skill_title_id": 1}, {"id": 3, "candidate_id_id": 3, "skill_title_id": 3}, {"id": 4, "candidate_id_id": 4, "skill_title_id": 1}, {"id": 5, "candidate_id_id": 4, "skill_title_id": 3}, {"id": 6, "candidate_id_id": 1, "skill_title_id": 3}, {"id": 7, "candidate_id_id": 4, "skill_title_id": 4}, {"id": 8, "candidate_id_id": 3, "skill_title_id": 6}, {"id": 9, "candidate_id_id": 5, "skill_title_id": 6}, {"id": 10, "candidate_id_id": 6, "skill_title_id": 5}, {"id": 11, "candidate_id_id": 7, "skill_title_id": 5}]
    load_table(skills, "candidates")
    load_table(candidates, "candidates")
    load_table(jobs, "jobs")
    load_table(job_requirements, "job_requirements")
    load_table(candidate_abilities, "candidate_abilities")


def load_table(data: list, table_name: str):
    #choose_item = {"skills": Skill(),"candidates":Candidate,"jobs":Job(),"job_requirements":JobRequirements(),"candidate_abilities":CandidatesAbilities}
    for data_item in data:
        if table_name == "skills":
            item = Skill()
        elif table_name == "candidates":
            item = Candidate()
        elif table_name == "jobs":
            item = Job()
        elif table_name == "job_requirements":
            item = JobRequirements()
        else:
            item = CandidatesAbilities()
        for k, v in data_item.items():
            setattr(item, k, v)
        item.save()
