from django.db import models


class Skill(models.Model):
    skill_text = models.CharField(max_length=200)
    jobs = models.ManyToManyField('Job', through='JobRequirements')
    candidates = models.ManyToManyField('Candidate', through='CandidatesAbilities')

    def __str__(self):
        return self.skill_text


class Candidate(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default="candidate")
    skills = models.ManyToManyField('Skill', through='CandidatesAbilities')

    def __str__(self):
        return f'{self.name, self.title}'


class Job(models.Model):
    title = models.CharField(max_length=200)
    skills = models.ManyToManyField('Skill', through='JobRequirements')

    def __str__(self):
        return self.title


class CandidatesAbilities(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill_title = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.candidate_id, self.skill_title}'


class JobRequirements(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill_title = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job_id, self.skill_title}'
