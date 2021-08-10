from django.shortcuts import render
from django.http import HttpResponse
from matchFinder.models import *
from rest_framework import status
from rest_framework.views import APIView


def find_candidates(request: APIView, job_id: int) -> list[Candidate]:
    """
    This function get a job and returns a list of candidates with a set of skills that is the closest to the set of skills
    required and also match to the job title.
    :param request: a GET request from browser
    :param job_id: the id matching to the job we want to match candidates to.
    :return: list of Candidates with the maximum amount of matching skills
    """
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist or AttributeError:
        return HttpResponse("Job Doesnt Exist")
    try:
        requirements = JobRequirements.objects.all().filter(job_id__jobrequirements=job_id).values('skill_title')
    except requirements.DoesNotExist:
        return HttpResponse("Job Doesnt have any skills set")
    try:
        matching_title_candidates = Candidate.objects.all().filter(title=job.title)
    except not matching_title_candidates.exists():
        return HttpResponse("No matching title in Candidates database")
    dic = create_match_dict(requirements, matching_title_candidates)
    try:
        max_matching_skills = max(dic.values())
    except ValueError:
        return HttpResponse("No matching Candidates")
    best_candidates = get_matching_candidates(max_matching_skills, dic)
    return HttpResponse(f'Candidates:{best_candidates}', 'a')


def get_matching_candidates(max_matching_skills: int, dic: dict) -> list[Candidate]:
    """
    creates a list of candidates that has maximum num of matching skills found in the candidates database.
    :param max_matching_skills: max num of matching skills found in the database.
    :param dic: key: candidate id, value: skills of the candidate that are in the job requirements
    :return: Final list to return to the user
    """
    top_candidates_ids = list()
    for key, value in dic.items():
        if value == max_matching_skills:
            top_candidates_ids.append(key)
    result = list()
    for candidate_id in top_candidates_ids:
        result.append(Candidate.objects.all().filter(id=candidate_id))
    return result


def create_match_dict(requirements: JobRequirements, matching_title_candidates: list[Candidate]) -> dict:
    """
    :param requirements: list of skills required for the job
    :param matching_title_candidates: list of candidates with matching title to the job title.
    :return: a dictionary of matching-title candidate as key and all skills that are also in the job requirements.
    """
    dic = dict()
    for candidate in matching_title_candidates:
        candidate_skills = CandidatesAbilities.objects.all().filter(candidate_id__candidatesabilities=candidate.id).values('skill_title')
        dic[candidate.id] = 0
        for requirement in requirements:
            if requirement in candidate_skills:
                dic[candidate.id] += 1
    return dic


def index(request):
    j = Job.objects.get(id=1)
    ans = find_candidates("", j.id)
    return ans


