from django.contrib import admin

from .models import Skill
from .models import Candidate
from .models import Job
from .models import JobRequirements
from .models import CandidatesAbilities


admin.site.register(Skill)
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(JobRequirements)
admin.site.register(CandidatesAbilities)

